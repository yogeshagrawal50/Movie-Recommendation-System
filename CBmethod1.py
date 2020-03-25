# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:44:22 2020

@author: hp
"""

import pandas as pd
import numpy as np

ratings= pd.read_csv('ratings.csv')
movies= pd.read_csv(r'movies.csv' )

ratings.loc[ratings['rating'] <= 3,  "rating"] = 0
ratings.loc[ratings['rating'] > 3,  "rating"] = 1


merged = ratings.merge(movies, left_on = 'movieId' , right_on = 'movieId', suffixes = ['_user',''])
merged = merged[['userId', 'title','genres','rating']]
merged = pd.concat([merged,merged['genres'].str.get_dummies(sep = '|')], axis = 1)
del merged['genres']
del merged['(no genres listed)']

cols = list(merged.columns.values)
cols.pop(cols.index('rating'))
merged = merged[cols+['rating']]

x = merged.iloc[:, 2:21]
y = merged.iloc[:,21].values

from sklearn.model_selection import train_test_split
x_train , x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

from sklearn.ensemble.forest import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 500, criterion = 'entropy', random_state = 0)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)

totalMovieIds = movies['movieId'].unique()

def nonratedmovies(userId):
    ratedmovies = ratings['movieId'].loc[ratings['userId'] == userId]
    non_ratedmovies = np.setdiff1d(totalMovieIds, ratedmovies.values)
    non_ratedmoviesDf = pd.DataFrame(non_ratedmovies, columns = ['movieId'])
    non_ratedmoviesDf['userId'] = userId
    non_ratedmoviesDf['predictions']=0
    active_user_nonratedmovies = non_ratedmoviesDf.merge(movies, left_on = 'movieId' , right_on = 'movieId', sort = True)
    active_user_nonratedmovies = pd.concat([active_user_nonratedmovies,active_user_nonratedmovies['genres'].str.get_dummies(sep = '|')], axis = 1)
    del active_user_nonratedmovies['genres']
    del active_user_nonratedmovies['(no genres listed)']
    del active_user_nonratedmovies['title']
    return (active_user_nonratedmovies)

active_user_nonratedmoviesDf = nonratedmovies(30)
df = active_user_nonratedmoviesDf.iloc[:,3:].values
y_pred2  = classifier.predict(df)
active_user_nonratedmoviesDf['prediction'] = y_pred2
recommend = active_user_nonratedmoviesDf[['movieId','prediction']]
recommend = recommend.loc[recommend['prediction'] == 1]

recommend.to_csv('recommend.csv', sep = ',',index = False)
