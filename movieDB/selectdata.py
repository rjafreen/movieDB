# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:04:37 2021

@author: DELL
"""

import sqlite3 as lit


db = lit.connect('mydatabase.db')



with db:
     cur = db.cursor()
     selectquery = "SELECT * FROM Movies WHERE actor = 'robert'"
     cur.execute(selectquery)
     
     
     
     
     row = cur.fetchall()
     
     
     for data in row:
         print(data)
         