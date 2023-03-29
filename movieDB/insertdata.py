# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:41:30 2021

@author: DELL
"""

import sqlite3 as lit



mymovie = (
    (1, 'Interstellar', 'Mathew', 'jessica', 'Christopher Nolan', '2014'),
    (2,'Avengers', 'robert','Scarlet', 'James', '2019'),
    (3, 'Gaurdians of galaxy', 'chris patt', 'zzoe saldana', 'Gunn', '2014'),
    (4, 'Sherelock Holmes', 'Doney jr', 'Rachael', 'Guy Ritchie', '2009'),
    (5, 'John wick3', 'Keanu Reeves', 'Halle', 'Chad Stakhelski', '2019'),
    )




db = lit.connect('mydatabase.db')


with db:
     cur = db.cursor()
     cur.executemany('INSERT INTO Movies VALUES(?,?,?,?,?,?)', mymovie)
     
     print("Data Inserted")
     