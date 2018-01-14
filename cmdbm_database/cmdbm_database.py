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

def menu_print():
    print("print menu")
    
def menu_modify():
    print("modify menu")

def main():
    
    menu = []
    
    menu_p = {'p', 'print', 'print a table', menu_print()} # use dictionary or list insted, no, make an object!
    menu_c = {'m', 'modify', 'modify an entry', menu_modify()}
    
    
    '''
    this is the main menu, you can either tell us to 
    print a table
    insert a new entry into a table
    or modify an entry within a table
    '''
    
    menu.append(menu_p)
    menu.append(menu_c)
    
    print(menu)
    print(menu[0])
    print(type(menu[0]))
    
    while True:
        
        print("  ")
        
        c = input("-->")
        
        print(c)
        if c == menu[0][0]:
            
            menu[0][3]()            
        elif c =='m':
            menu_modify()
        elif c == 'i':
            
            d = bm_database.connect()
            bm_database.setup_db(d)

            bm_database.push_into_matter_of_expense(d, "Frisoer Benedikt", 1, 1, 1, 20, "monthly", 1)
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