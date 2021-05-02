# -*- coding: utf-8 -*-
"""
Created on Sat May  1 13:41:18 2021

@author: Prthamesh
"""

import pandas as pd

def get_data():
    user_ratings_df = pd.read_hdf(r'C:\Users\Prthamesh\Downloads\ml-latest-small\prepared_matrices.h5','user_ratings_df')
    movie_attributes_df = pd.read_hdf(r'C:\Users\Prthamesh\Downloads\ml-latest-small\prepared_matrices.h5','movie_attributes_df')
    movie_titles_df = pd.read_hdf(r'C:\Users\Prthamesh\Downloads\ml-latest-small\prepared_matrices.h5','movie_titles')
    user_ratings_df.fillna(0,inplace=True)
    return {'user_ratings_df':user_ratings_df,'movie_attributes_df':movie_attributes_df,'movie_titles_df':movie_titles_df}

