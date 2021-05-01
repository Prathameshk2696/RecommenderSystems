# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:25:36 2021

@author: Prthamesh
"""
import numpy as np
import pandas as pd

class CollaborativeFiltering:
    
    def __init__(self,approach = 'knn',movie_data):
        
        self.user_id = None
        self.name = 'Collaborative Based Filtering'
        self.approach = approach
        self.number_of_collaborators = None
        self.number_movie_recommendations = None
        self.user_ratings_df = movie_data['user_ratings_df']
        self.movie_attributes_df = movie_data['movie_attributes_df']
        self.movie_titles_df = movie_data['movie_titles_df']
        
    
    def get_input():
        self.user_id = int(input('Enter User ID: '))
        self.number_of_collaborators = int(input('Enter User ID: '))
        self.number_movie_recommendations = self.number_movie_recommendations = int(input('Enter number of movies to be recommended : '))
        
    def find_distance(item_1,item_2):
        distance = np.linalg.norm(item_1-item_2)
        return distance
    
    def compute_distance_with_all_users(self):
        
        distance_user={}
        rating_of_user = self.user_ratings_df.iloc[self.user_id]
        specific_user_ratings = rating_of_user.to_numpy()
        
        for row in self.user_ratings_df.iterrows():
            if(row[0]!=self.user_id):
                distance_user[row[0]]=(find_distance(row[1].to_numpy(),specific_user_ratings),row[1].to_numpy())
        return distance_user
    
    def compute_kNearest_users(self,distance_dict):
        top_k_collaborators = dict(sorted(distance_dict.items(), key=lambda x:x[1][0])[:self.number_of_collaborators])
        return top_k_collaborators
    
    
    def compute_weighted_movie_rating(self,neighbors):
    
        sum_distance=0
        movie_ratings=0
        sum_distance=0
        
        watched = np.where(self.user_ratings_df.iloc[userid]>0,0,1)
        
        for k,v in neighbors.items():
            
            sum_distance+=v[0]
            
        for k,v in neighbors.items():
            movie_ratings+=(v[0]*v[1])/sum_distance
        
        
        return movie_ratings*watched
        
    def get_topk_recommendations(self):
          
        top_k_recommendations = self.movie_attributes_df.argsort()[-self.number_movie_recommendations:][::-1]
        return top_k_recommendations
    
    def recommend(self):
        
        distance_user = self.compute_distance_with_all_users(self)
        
        k_collaborators = self.compute_kNearest_users(self,distance_user)
        
        weighted_movie_ratings = self.compute_weighted_movie_rating(self,k_users)
        
        top_k_movies = self.get_topk_recommendations(self,weighted_movie_ratings)
       
        headers = ['Movie Id','Movie Name','Year']
        table = []
        for movie_id in top_k_movies:
            table.append([movie_id,self.movie_titles_df.loc[movie_id,'title'],self.movie_titles_df.loc[movie_id,'year']])
        print(tabulate(table,headers,tablefmt='grid'))
        
      
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
        
    
    