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
from cmdbm_database_print import *

class c_menu_delete():
    ''' print menu
    '''
     
    def __init__(self):
         
        mod_logging_mkI_PYTHON.c_logging.__init__(self, 'cmd')
         
        # we need a variable which holds the main menu    
        self.menu_delete = []
        self.menu_delete.append(c_menu_items('me', 'members', 'member table', self.members))
        self.menu_delete.append(c_menu_items('ex', 'matter of expense', 'matter of expense', self.matter_of_expense))  
        self.menu_delete.append(c_menu_items('in', 'invoices', 'invoices', self.invoices))
        self.menu_delete.append(c_menu_items('gm', 'groups of members', 'groups of members', self.groups_of_members))
        self.menu_delete.append(c_menu_items('ge', 'groups of expenses', 'groups of expenses', self.groups_of_expenses))
        self.menu_delete.append(c_menu_items('ea', 'earnings', 'earnings', self.earnings))
        self.menu_delete.append(c_menu_items('ac', 'accounts', 'accounts', self.accounts))
        self.menu_delete.append(c_menu_items('cl', 'classes', 'classes', self.classes))
        return
     
    def members(self):
        ''' insert into members entries
        '''
         
        # push a message to the logger
        self.logger.warn('members')
     
        # show the existing members
        menu_print = c_menu_print()
        menu_print.members()        
     
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_members = c_bm_table_members(conn, cursor)
         
        # now, push it to the table
        ret = bm_table_members.select_matching_id(row)
        if (ret != None):
            bm_table_members.pop(ret)
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def matter_of_expense(self):
        ''' insert into matter of expense
         
        '''
         
        # push a message to the logger
        self.logger.warn('matter of expense')
         
        # print the current items
        menu_print = c_menu_print()
        menu_print.matter_of_expense()
         
        # ask the user for specific inputs
        nr = input("\t\t id = ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_matter_of_expenses = c_bm_table_matter_of_expenses(conn, cursor)
         
        # now, push it to the table
        
        bm_table_matter_of_expenses.pop()
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def invoices(self):
        ''' insert into the invoices table
        '''
         
        # push a message into the logger
        self.logger.warn('matter of invoices')
 
        # print the current items
        menu_print = c_menu_print()
        menu_print.invoices()
         
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_invoices = c_bm_table_invoices(conn, cursor)
         
        # now, push it to the table
        
        bm_table_invoices.pop()
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def groups_of_members(self):
        ''' insert into the group of members table
        '''
         
        # push a message into the logger
        self.logger.warn('groups of members')
 
        # print the current items
        menu_print = c_menu_print()
        menu_print.groups_of_members()
 
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_groups_of_members = c_bm_table_groups_of_members(conn, cursor)
         
        # now, push it to the table
        
        bm_table_groups_of_members.pop()
         
        # now, disconnect again
        bm_database.disconnect()
        return   
     
     
    def groups_of_expenses(self):
        ''' insert into the group of expenses tables
        '''
         
        # push a message into the logger
        self.logger.warn('groups of expenses')
 
        # print the current items
        menu_print = c_menu_print()
        menu_print.groups_of_expenses()
 
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_groups_of_expenses = c_bm_table_groups_of_expenses(conn, cursor)
         
        # now, push it to the table
        
        bm_table_groups_of_expenses.pop()
         
        # now, disconnect again
        bm_database.disconnect()
        return 
     
    def earnings(self):
        ''' print the earnings entries
        '''
         
        # push a message into the logger
        self.logger.warn('earnings')
 
        # print the current items
        menu_print = c_menu_print()
        menu_print.earnings()
 
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_earnings = c_bm_table_earnings(conn, cursor)
         
        # now, push it to the table
        
        bm_table_earnings.pop()
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def accounts(self):
        ''' print the accounts entries
        '''
         
        # push a message into the logger
        self.logger.warn('accounts')
 
        # print the current items
        menu_print = c_menu_print()
        menu_print.groups_of_expenses()
 
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_accounts = c_bm_table_accounts(conn, cursor)
         
        # now, push it to the table
        
        bm_table_accounts.pop()
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def classes(self):
        ''' print the classes entries
        '''
         
        # push a message into the logger
        self.logger.warn('classes')
 
        # print the current items
        menu_print = c_menu_print()
        menu_print.groups_of_expenses()
 
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_classes = c_bm_table_classes(conn, cursor)
         
        # now, push it to the table
        
        bm_table_classes.pop()
         
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
            for cnt in range(0, len(self.menu_delete)):
                print("{}\t{}".format(self.menu_delete[cnt].get_cmd(), self.menu_delete[cnt].get_help_text()))
             
            c = input("-->")
             
            print(c)
 
            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_delete)):
                if c == self.menu_delete[cnt].cmd:
                    print(self.menu_delete[cnt].get_help_text())
                    self.menu_delete[cnt].fun()
            
            if c =='q':
                break

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()