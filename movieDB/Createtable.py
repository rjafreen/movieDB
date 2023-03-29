# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:05:03 2021

@author: DELL
"""

import sqlite3 as lit




def main():
    try:
        db = lit.connect('mydatabase.db')
        cur = db.cursor()
        
        
        tablequery = "CREATE TABLE Movies(id INT, name TEXT, actor TEXT, actress TEXT, director TEXT, yearOf_Release TEXT)"
        
        
        cur.execute(tablequery)
        print("Table Created")
        
        
        
    except lit.Error as e:
           print("Unable to create Table")
           
           
           
           
           
if __name__ == '__main__':
    main()
           