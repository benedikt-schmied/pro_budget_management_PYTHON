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
sys.path.append('./../bm_database')
sys.path.append('./../mod_logging_mkI_PYTHON')
import sqlite3
import os
import argparse
from bm_database import *
import mod_logging_mkI_PYTHON
from cmdmenu import *
from cmdbm_database_setup import *

class c_menu_calc():
    ''' print menu
    '''
     
    def __init__(self):
         
        mod_logging_mkI_PYTHON.c_logging.__init__(self, 'cmd.warn')
         
        # we need a variable which holds the main menu    
        self.menu_calc = []
        self.menu_calc.append(c_menu_items('te', 'total_expenses', 'give me the total expenses', self.total_expenses))
        return
     
    def total_expenses(self):
        ''' calc the total expenses
        '''
         
        # push a message to the logger
        self.logger.warn('members')
         
        # connect to the database
        d = bm_database.connect()
         
        # now, push it to the table
        entries = []
        entries = bm_database.get_entries_matter_of_expense(d)
        amount = 0
        for item in entries:
            print("\t\t name = {}, amount = {}, frequency = {}".format(item[1], item[7], item[8]))
             
            if item[8] > 4:
                divider = item[8] / 4
                amount = amount + (item[7] / divider)
            else:
                amount = amount + (item[7])
         
        entries = []
        entries = bm_database.get_entries_earnings(d)
        earnings = 0
        for item in entries:
            print("\t\t name = {}, account = {}, amount = {}".format(item[1], item[2], item[3]))
            earnings = earnings + item[3]
         
        print("\t\t amount = {}, which means, we've got an income of {}, spare {}".format(amount, earnings, earnings - amount))
         
        # now, disconnect again
        bm_database.disconnect(d)
        return
     
    def run(self):
         
        '''
        this is the main menu, you can either tell us to 
        print a table
        insert a new entry into a table
        or modify an entry within a table
        '''    
        self.logger.warn('running')
        while True:
             
            # first print the menu
            for cnt in range(0, len(self.menu_calc)):
                print("{}\t{}".format(self.menu_calc[cnt].get_cmd(), self.menu_calc[cnt].get_help_text()))
             
            c = input("-->")
             
            print(c)
 
            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_calc)):
                if c == self.menu_calc[cnt].cmd:
                    print(self.menu_calc[cnt].get_help_text())
                    self.menu_calc[cnt].fun()
            
            if c =='q':
                break

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()