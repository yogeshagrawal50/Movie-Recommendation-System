# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:52:51 2020

@author: hp
"""

import pandas as pd
from sklearn.neighbors import NearestNeighbors


movies= pd.read_csv(r'movies.csv' )

movies = pd.concat([movies,movies['genres'].str.get_dummies(sep = '|')], axis = 1)
del movies['genres']
del movies['(no genres listed)']

selected = [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
X = movies.iloc[:, 2:21]

nbrs = NearestNeighbors(n_neighbors = 5).fit(X)
print(nbrs.kneighbors([selected]))