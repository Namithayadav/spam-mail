# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:12:53 2023

@author: Namitha
"""

from deta import Deta
DETA_KEY="d03mix7x_d4r91nQ3Cbx92WGepYpcVUq5RP7CmaiQ"
# Initialize with a project key
deta = Deta(DETA_KEY)
# This is how to create/connect a database
db = deta.Base("Users_data")

def insert_data(input1,result):
    return db.put({"Text":input1,"Result":result})