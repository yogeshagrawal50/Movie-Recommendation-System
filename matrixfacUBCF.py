# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 17:58:24 2020

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

def recommend_movies(prediction_df, user_ID, movies_df, original_ratings_df, num_recommendations=5):
    
    user_row_number = user_ID-1
    sorted_user_predictions = predicted_rating_df.iloc[user_row_number].sort_values(ascending=False)
    
    user_data = original_ratings_df[original_ratings_df.userId ==(user_ID)]
    user_full = (user_data.merge(movies_df, how = 'left', left_on = 'movieId', right_on = 'movieId').sort_values(['rating'], ascending = False))
    print('user {0} has alreqady rated {1} movies.'.format(user_ID, user_full.shape[0]))
    print('Recommending highest {0} prdicted ratingss movies not alreadyrated.'.format(num_recommendations))
    
    recommendations = (movies_df[~movies_df['movieId'].isin(user_full['movieId'])].
                       merge(pd.DataFrame(sorted_user_predictions).reset_index(),how = 'left',
                             left_on = 'movieId', right_on = 'movieId').
                             sort_values(['rating'], ascending = False).
                             iloc[:num_recommendations, :-1])
                       
    return user_full, recommendations

already_rated ,predictions = recommend_movies(predicted_rating_df,2,movies_df,rating_df,10)
already_rated = already_rated.head(10)
predictions = predictions















