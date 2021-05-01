# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:25:36 2021

@author: Prthamesh
"""

import pandas as pd

class CollaborativeFiltering:
    
    def __init__(self,approach = 'knn'):
        pass
    
    def get_input():
        pass
    
class ContentBasedFiltering:
    
    def __init__(self):
        self.user_id = None
        self.name = 'Content Based Filtering'
        self.number_movie_recommendations = None
    
    def get_input(self):
        self.user_id = int(input('Enter User ID : '))
        self.number_movie_recommendations = int(input('Enter number of movies to be recommended : '))
        
    def compute_similarity(watched_movie_ids):
    unwatched_movie_ids = movie_attributes_df.index.difference(watched_movie_ids)
    dist_df = pd.DataFrame(index=unwatched_movie_ids,columns=watched_movie_ids)
    unwatched_movie_attributes_df = movie_attributes_df.loc[unwatched_movie_ids]
    for movie_id in watched_movie_ids:
        dist_df.loc[:,movie_id] = (((unwatched_movie_attributes_df - movie_attributes_df.loc[movie_id,:])**2).sum(axis=1))**0.5
    return dist_df

def get_watched_movies(user_id):
    return user_ratings_df.loc[user_id,user_ratings_df.loc[user_id].notnull()].index

def get_recommendations(user_id,k = 5):
    watched_movie_ids = get_watched_movies(user_id)
    dist_df = compute_similarity(watched_movie_ids)
    return list(dist_df.min(axis=1).nsmallest(k).index)
        
    def recommend(self):
        
    
    