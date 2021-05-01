# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:28:49 2021

@author: Prthamesh
"""

from recommend.recommenders import ContentBasedFiltering
from recommend.recommenders import CollaborativeFiltering

if __name__ == '__main__':
    
    message = ('Press 1 for collaborative filtering using k-nearest neighbors\n'+
               'Press 2 for collaborative filtering using SVD'+
               'Press 3 for content-based filtering')
    
    recommender_name = int(input(message))
    
    if recommender_name in {1,2}:
        rs = CollaborativeFiltering()
    elif recommender_name == 3:
        rs = ContentBasedFiltering()
    
    print(rs.recommend())
    
    
    
    