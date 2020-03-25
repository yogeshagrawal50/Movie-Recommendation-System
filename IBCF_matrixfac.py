# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:40:30 2020

@author: hp
"""

'''
Matrix Factorization  
movie ratings  = user attricutes x movie attributes


single value decompostion
A(mxn) = U(mxr)D(rxr)V(transponse)(rxn)

u and v are orthonormal
D is diagonal
U(transponse)U = I(mxm)
V(transponse)V = I(nxn)

r: The rank of a matrix is the number of linerarly independent rows or columns in the matrxix

step 1: represent the data set as a matrix where the user are rows , movies are columns and the individuals entries are specific ratings
step 2: transform nan values to 0s
strp 3: normalize the data
step 4: choose k(using th cross validation)
'''
import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds
from sklearn.metrics.pairwise import cosine_similarity

rating_df= pd.read_csv('ratings.csv')
movies_df= pd.read_csv(r'movies.csv' )

A_df = rating_df.pivot_table(index = ['userId'], columns = ['movieId'], values ='rating', aggfunc = np.max)
A_df.replace({np.nan:0},inplace=True)

A  = A_df.as_matrix()

user_ratings_mean = np.mean(A, axis = 1)
A_normalized = A - user_ratings_mean.reshape(-1,1)

U, sigma,Vt = svds(A_normalized, k = 50)

sigma = np.diag(sigma)

predicted_rating = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1,1)

predicted_rating_df = pd.DataFrame(predicted_rating, columns = A_df.columns)
preds_df = np.transpose(predicted_rating_df)

item_similarity = cosine_similarity(preds_df)

item_sim_df = pd.DataFrame(item_similarity, index = preds_df.index,  columns = preds_df.index)

def sim_movies(movieId):
    count = 1
    movieindex = movies_df.index[movies_df['movieId'] == movieId]
    print("Similar movies to {} are :".format(movies_df.loc[movieindex].title))
    for item in item_sim_df.sort_values(by = movieId, ascending = False).index[1:11]:
        itemIndex = movies_df.index[movies_df['movieId']==item]
        print('No, {}:{}'.format(count, movies_df.loc[itemIndex].title))
        count+=1
        
sim_movies(89745)


