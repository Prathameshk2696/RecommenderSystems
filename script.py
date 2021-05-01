# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:28:49 2021

@author: Prthamesh
"""

import data_reader as dr
from recommend.recommenders import ContentBasedFiltering
from recommend.recommenders import CollaborativeFiltering

if __name__ == '__main__':
    
    movie_data = dr.get_data() # 
    
    message = ('Press 1 for collaborative filtering using k-nearest neighbors\n'+
               'Press 2 for collaborative filtering using SVD\n'+
               'Press 3 for content-based filtering\n')
    
    recommender_name = int(input(message))
    
    if recommender_name in {1,2}:
        rs = CollaborativeFiltering(movie_data)
    elif recommender_name == 3:
        rs = ContentBasedFiltering(movie_data)
    
    print(rs.recommend())
    
    
    
    