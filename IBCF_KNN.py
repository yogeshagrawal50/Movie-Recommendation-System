# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:21:55 2020

@author: hp
"""

import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

ratings= pd.read_csv('ratings.csv')
movies= pd.read_csv(r'movies.csv' )

merged = ratings.merge(movies, left_on = 'movieId' , right_on = 'movieId', suffixes = ['_user',''])
merged.rename(columns = {'rating_user':'user_rating'}, inplace = True)
merged = merged[['userId', 'title','rating']]

movieratings  =  merged.pivot_table(index = ['title'], columns = ['userId'], values = 'rating') #creating pivot table for cosine function

movieratings.replace({np.nan:0}, inplace = True)

model_knn = NearestNeighbors(algorithm='brute',metric = 'cosine')
model_knn.fit(movieratings.values)

distances, indices = model_knn.kneighbors(movieratings.iloc[60,:].values.reshape(1,-1), n_neighbors = 6)

for i in range(0, len(distances.flatten())):
    if  i == 0:
        print("Recommendation for {0}:".format(movieratings.index[60]))
    else:
        print("{0}:{1}, with distance of {2}".format(i, movieratings.index[indices.flatten()[i]], distances.flatten()[i]))