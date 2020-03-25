# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import operator

ratings= pd.read_csv('ratings.csv')

movies= pd.read_csv(r'movies.csv' )

merged = ratings.merge(movies, left_on = 'movieId' , right_on = 'movieId', sort = True)
merged = merged[['userId', 'title','rating']]

movieratings  =  merged.pivot_table(index = ['userId'], columns = ['title'], values = 'rating') #creating pivot table for cosine function

movieratings.replace({np.nan:0}, inplace = True)

user_similarity = cosine_similarity(movieratings)

user_sim_df = pd.DataFrame(user_similarity, index = movieratings.index,  columns = movieratings.index)
movieratings = movieratings.T

def recommendation(user):
    if user not in movieratings.columns:
        return('No data available on this user')
        
    sim_user = user_sim_df.sort_values(by = user, ascending = False).index[1:11] #creating a df of similar users
    
    best = []
    for i in sim_user:
        max_score = movieratings.loc[:,i].max() 
        best.append(movieratings[movieratings.loc[:,user] == max_score].index.tolist())
        
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
    return(sorted_list)
    
recommendation(5)
print(recommendation(5))
