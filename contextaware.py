# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:04:26 2020

@author: hp
"""

import pandas as pd
import numpy as np

ratings= pd.read_csv('ratings.csv')
movies= pd.read_csv(r'movies.csv' )
ts  = ratings['timestamp']
ts = pd.to_datetime(ts, unit = 's').dt.hour
movies['hours']  = ts


merged = ratings.merge(movies, left_on = 'movieId' , right_on = 'movieId', suffixes = ['_user',''])
merged = merged[['userId', 'movieId','genres','hours']]
merged = pd.concat([merged,merged['genres'].str.get_dummies(sep = '|')], axis = 1)
del merged['genres']
del merged['(no genres listed)']


def activateuserprofile(userId):
    userprofile = merged.loc[merged['userId'] == userId]
    del userprofile ['userId']
    del userprofile['movieId']
    userprofile = userprofile.groupby(['hours'], as_index = False, sort =True).sum()
    userprofile.iloc[:,1:20] = userprofile.iloc[:,1:20].apply(lambda x:(x - np.min(x))/(np.max(x)-np.min(x)),axis = 1)
    return(userprofile)                                                                                                                                                                                                                                                                                                                                                                                                                    

activeuser = activateuserprofile(30)

recommend = movies= pd.read_csv(r'recommend.csv' )
del merged['userId']
del merged['rating']

merged = merged.drop_duplicate()

user_pref = recommend.merge(merged, left_on = 'movieId' , right_on = 'movieId', suffixes = ['_user',''])
product = np.dot(user_pref.iloc[:,2:21].as_matrix(), activeuser.iloc[21,2:21].as_matrix())#IndexError: single positional indexer is out-of-bounds

preferences  = np.stack((user_pref['movieId'], product), axis  =-1)
df = pd.DataFrame(preferences, columns = ['movieId', 'prefrernces'])
result = (df.sort_values(['preferences'], ascending = False).iloc[0:10],0)
