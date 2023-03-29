# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 12:56:10 2021

@author: DELL
"""

import sqlite3 as lit




def main():
    try:
        db = lit.connect('mydatabase.db')
        print("Database Created", db)
        
    except:
        print("Failed to create Database")
        
        
        
        
        
        
        
if __name__ == '__main__':
    main()
        
        