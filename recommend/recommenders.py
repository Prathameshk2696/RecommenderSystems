# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:25:36 2021

@author: Prthamesh
"""

import pandas as pd
from tabulate import tabulate

class CollaborativeFiltering:
    
    def __init__(self,approach = 'knn'):
        pass
    
    def get_input():
        pass
    
class ContentBasedFiltering:
    
    def __init__(self,movie_data):
        self.user_id = None
        self.name = 'Content Based Filtering'
        self.number_movie_recommendations = None
        self.user_ratings_df = movie_data['user_ratings_df']
        self.movie_attributes_df = movie_data['movie_attributes_df']
        self.movie_titles_df = movie_data['movie_titles_df']
        self.get_input()
    
    def get_input(self):
        self.user_id = int(input('Enter User ID : '))
        self.number_movie_recommendations = int(input('Enter number of movies to be recommended : '))
        
    def compute_similarity(self,watched_movie_ids):
        unwatched_movie_ids = self.movie_attributes_df.index.difference(watched_movie_ids)
        dist_df = pd.DataFrame(index=unwatched_movie_ids,columns=watched_movie_ids)
        unwatched_movie_attributes_df = self.movie_attributes_df.loc[unwatched_movie_ids]
        for movie_id in watched_movie_ids:
            dist_df.loc[:,movie_id] = (((unwatched_movie_attributes_df - self.movie_attributes_df.loc[movie_id,:])**2).sum(axis=1))**0.5
        return dist_df
        
    def recommend(self):
        watched_movie_ids = self.user_ratings_df.loc[self.user_id,self.user_ratings_df.loc[self.user_id].notnull()].index
        dist_df = self.compute_similarity(watched_movie_ids)
        recommended_movie_ids = list(dist_df.min(axis=1).nsmallest(self.number_movie_recommendations).index)
        headers = ['Movie Id','Movie Name','Year']
        table = []
        for movie_id in recommended_movie_ids:
            table.append([movie_id,self.movie_titles_df.loc[movie_id,'title'],self.movie_titles_df.loc[movie_id,'year']])
        print(tabulate(table,headers,tablefmt='grid'))
        
        
        
        