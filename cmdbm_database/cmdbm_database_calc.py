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
         
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name + ".calc")
         
        # we need a variable which holds the main menu    
        self.menu_calc = []
        self.menu_calc.append(c_menu_items('te', 'total_expenses', 'give me the total expenses', self.total_expenses))
        return
     
    def total_expenses(self):
        ''' calc the total expenses
        '''
         
        # push a message to the logger
        self.logger.warn('total expenses')
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
         
        # create a member class
        bm_table_matter_of_expenses = c_bm_table_matter_of_expenses(conn, cursor)
        bm_table_matter_of_expenses.show_all_l()
        
        bm_table_earnings = c_bm_table_earnings(conn, cursor)
        bm_table_earnings.show_all_l()
        
        amount = 0
        
        for item in bm_table_matter_of_expenses.get_all():
            print("\t\t name = {}, amount = {}, frequency = {}".format(item.name, item.amount, item.frequency))
             
            if item.frequency > 4:
                divider = item.frequency / 4
                amount = amount + (item.amount / divider)
            else:
                amount = amount + (item.amount)
         

        earnings = 0
        for item in bm_table_earnings.get_all():
            print("\t\t name = {}, account = {}, amount = {}".format(item.name, item.account, item.amount))
            earnings = earnings + item.amount

        print("\t\t amount = {}, which means, we've got an income of {}, spare {}".format(amount, earnings, earnings - amount))
         
        # now, disconnect again
        bm_database.disconnect()
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