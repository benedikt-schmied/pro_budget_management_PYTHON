#!/usr/bin/python3
# coding=latin-1

'''
creation date
author 

objectives:

small command line interface that lets you insert basic
information in each table, that lets you search within
a table and which prints human readable information 
'''

import sys
import sqlite3
import os
import argparse
import bm_database
import sys

def main():
    
    while True:
        c = input("-->")
        print(c)
        if c == 'p':
            break
            
        elif c =='s':
            break
        elif c == 'i':
            
            d = bm_database.connect()
            bm_database.setup_db(d)

            bm_database.push_into_matter_of_expense(d, "Frisoer Benedikt", 1, 1, 1, 20, "monthly", 1)
            break

        elif c == 'r':
            
            d = bm_database.connect()
            bm_database.setup_db(d)
            
            print(bm_database.get_entries_matter_of_expense(d))
            
            entry = bm_database.get_entries_matter_of_expense(d)
            bm_database.disconnect(d)
            a = 0
            for cnti in entry:
                str='{}'.format(cnti[0])
                a = a + 2
                
            break

        elif c == 'q':
            break  # Exit the while loop

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
  
    c = bm_database.connect()
    bm_database.setup_db(c)
    bm_database.push_into_matter_of_expense(c, "Friser Termin", 1, 1, 1, 20, 1, 1)
    bm_database.push_into_matter_of_expense(c, "Friseur Termin", 1, 1, 1, 20, 1, 1)
    bm_database.push_into_matter_of_expense(c, "Frisir Termin", 1, 1, 1, 20, 1, 1)
    bm_database.push_into_matter_of_expense(c, "Fresir Termin", 1, 1, 1, 20, 1, 1)
    
    entries=[]
    entries=bm_database.get_entries_matter_of_expense(c)
    for cnti in entries:
        print(cnti)
    bm_database.disconnect(c) 
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()
    main()