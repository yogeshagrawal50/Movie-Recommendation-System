# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:16:43 2020

@author: hp
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import operator

ratings= pd.read_csv('ratings.csv')

movies= pd.read_csv(r'movies.csv' )

merged = ratings.merge(movies, left_on = 'movieId' , right_on = 'movieId', sort = True)
merged = merged[['userId', 'title','rating']]

movieratings  =  merged.pivot_table(index = ['title'], columns = ['userId'], values = 'rating') #creating pivot table for cosine function

movieratings.replace({np.nan:0}, inplace = True)

item_similarity = cosine_similarity(movieratings)

item_sim_df = pd.DataFrame(item_similarity, index = movieratings.index,  columns = movieratings.index)

def sim_movies(title):
    count = 1
    print("Similar movies to {} are :".format(title))
    for item in item_sim_df.sort_values(by = title, ascending =False).index[1:11]:
        print('No, {}:{}'.format(count, item))
        count+=1
        
sim_movies('Jumanji (1995)')