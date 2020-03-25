# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:46:07 2020

@author: hp
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import operator

ratings= pd.read_csv('ratings.csv')
movies= pd.read_csv(r'movies.csv' )

merged = ratings.merge(movies, left_on = 'movieId' , right_on = 'movieId', sort = True)
merged = merged[['userId', 'title','rating']]

movieratings = merged.pivot_table(index = ['userId'], columns = ['title'], values = 'rating') #creating pivot table for cosine function

movieratings.replace({np.nan:0}, inplace = True)

model_knn = NearestNeighbors(algorithm='brute',metric = 'cosine')
model_knn.fit(movieratings.values)

user  = 2
distances, indices = model_knn.kneighbors(movieratings.iloc[user-1,:].values.reshape(1,-1), n_neighbors = 7)

best = []
movieratings = movieratings.T
for i in indices.flatten():
    if(i!= user-1):
        max_score = movieratings.loc[:,i+1].max() 
        best.append(movieratings[movieratings.loc[:,i+1] == max_score].index.tolist())
    
user_seen_movies = movieratings[movieratings.loc[:,user] > 0].index.tolist()

for i in range(len(best)):
    for j in best[i]:
        if (j in user_seen_movies):
            best[i].remove(j)
most_common = {}
for i in range(len(best)):
    for j in best[i]:
        for j in best[i]:
            if j in most_common:
                most_common[j] += 1
            else:
                most_common[j] = 1
                
sorted_list = sorted(most_common.items(), key = operator.itemgetter(1), reverse  =True)
sorted_list[:5]