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
import bm_table_matter_of_expenses
sys.path.append('./../bm_database')
sys.path.append('./../mod_logging_mkI_PYTHON')
import sqlite3
import os
import argparse
from bm_database import *
import mod_logging_mkI_PYTHON
from cmdmenu import *
from cmdbm_database_print import *

class c_menu_insert():
    ''' print menu
    '''
     
    def __init__(self):
         
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name + ".insert")
         
        # we need a variable which holds the main menu    
        self.menu_insert = []
        self.menu_insert.append(c_menu_items('me', 'members', 'member table', self.members))
        self.menu_insert.append(c_menu_items('ex', 'matter of expense', 'matter of expense', self.matter_of_expenses))  
        self.menu_insert.append(c_menu_items('in', 'invoices', 'invoices', self.invoices))
        self.menu_insert.append(c_menu_items('gm', 'groups of members', 'groups of members', self.groups_of_members))
        self.menu_insert.append(c_menu_items('ge', 'groups of expenses', 'groups of expenses', self.groups_of_expenses))
        self.menu_insert.append(c_menu_items('ea', 'earnings', 'earnings', self.earnings))
        self.menu_insert.append(c_menu_items('ac', 'accounts', 'accounts', self.accounts))
        self.menu_insert.append(c_menu_items('cl', 'classes', 'classes', self.classes))
        return
     
    def members(self):
        ''' insert into members entries
        '''
         
        # push a message to the logger
        self.logger.warn('members')
         
        # show all members so far
        menu_print = c_menu_print()
        menu_print.members()
        
        # we need a generic list in order to fetch the items
        args = []
        
        # loop and fetch the entries
        for item in t_bm_table_members_s._fields:
            args.append(input("\t\t <--> give us the {}:  ".format(item)))
            if not args[-1]:
                return 0

        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_members = c_bm_table_members(conn, cursor)
        
        # push the entries into the table 
        bm_table_members.push(t_bm_table_members_s._make(args))
        
        # now, disconnect again
        bm_database.disconnect()
        return
#     
    def matter_of_expenses(self):
        ''' insert into matter_of_expenses entries
        '''
         
        # push a message to the logger
        self.logger.warn('matter_of_expenses')
         
        # show all matter_of_expenses so far
        menu_print = c_menu_print()
        menu_print.matter_of_expenses()
        
        # we need a generic list in order to fetch the items
        args = []
        
        # loop and fetch the entries
        for item in t_bm_table_matter_of_expenses_s._fields:
            args.append(input("\t\t <--> give us the {}:  ".format(item)))
            if not args[-1]:
                return 0

        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_matter_of_expenses = c_bm_table_matter_of_expenses(conn, cursor)
        
        # push the entries into the table 
        bm_table_matter_of_expenses.push(t_bm_table_matter_of_expenses_s._make(args))
        
        # now, disconnect again
        bm_database.disconnect()
        return
#     
    def invoices(self):
        ''' insert into invoices entries
        '''
         
        # push a message to the logger
        self.logger.warn('invoices')
         
        # show all invoices so far
        menu_print = c_menu_print()
        menu_print.invoices()
        
        # we need a generic list in order to fetch the items
        args = []
        
        # loop and fetch the entries
        for item in t_bm_table_invoices_s._fields:
            args.append(input("\t\t <--> give us the {}:  ".format(item)))
            if not args[-1]:
                return 0

        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_invoices = c_bm_table_invoices(conn, cursor)
        
        # push the entries into the table 
        bm_table_invoices.push(t_bm_table_invoices_s._make(args))
        
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def groups_of_members(self):
        ''' insert into groups_of_members entries
        '''
         
        # push a message to the logger
        self.logger.warn('groups_of_members')
         
        # show all groups_of_members so far
        menu_print = c_menu_print()
        menu_print.groups_of_members()
        
        # we need a generic list in order to fetch the items
        args = []
        
        # loop and fetch the entries
        for item in t_bm_table_groups_of_members_s._fields:
            args.append(input("\t\t <--> give us the {}:  ".format(item)))
            if not args[-1]:
                return 0

        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_groups_of_members = c_bm_table_groups_of_members(conn, cursor)
        
        # push the entries into the table 
        bm_table_groups_of_members.push(t_bm_table_groups_of_members_s._make(args))
        
        # now, disconnect again
        bm_database.disconnect()
        return
     
     
    def groups_of_expenses(self):
        ''' insert into groups_of_expenses entries
        '''
         
        # push a message to the logger
        self.logger.warn('groups_of_expenses')
         
        # show all groups_of_expenses so far
        menu_print = c_menu_print()
        menu_print.groups_of_expenses()
        
        # we need a generic list in order to fetch the items
        args = []
        
        # loop and fetch the entries
        for item in t_bm_table_groups_of_expenses_s._fields:
            args.append(input("\t\t <--> give us the {}:  ".format(item)))
            if not args[-1]:
                return 0

        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_groups_of_expenses = c_bm_table_groups_of_expenses(conn, cursor)
        
        # push the entries into the table 
        bm_table_groups_of_expenses.push(t_bm_table_groups_of_expenses_s._make(args))
        
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def earnings(self):
        ''' insert into earnings entries
        '''
         
        # push a message to the logger
        self.logger.warn('earnings')
         
        # show all earnings so far
        menu_print = c_menu_print()
        menu_print.earnings()
        
        # we need a generic list in order to fetch the items
        args = []
        
        # loop and fetch the entries
        for item in t_bm_table_earnings_s._fields:
            args.append(input("\t\t <--> give us the {}:  ".format(item)))
            if not args[-1]:
                return 0

        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_earnings = c_bm_table_earnings(conn, cursor)
        
        # push the entries into the table 
        bm_table_earnings.push(t_bm_table_earnings_s._make(args))
        
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def accounts(self):
        ''' insert into accounts entries
        '''
         
        # push a message to the logger
        self.logger.warn('accounts')
         
        # show all accounts so far
        menu_print = c_menu_print()
        menu_print.accounts()
        
        # we need a generic list in order to fetch the items
        args = []
        
        # loop and fetch the entries
        for item in t_bm_table_accounts_s._fields:
            args.append(input("\t\t <--> give us the {}:  ".format(item)))
            if not args[-1]:
                return 0

        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_accounts = c_bm_table_accounts(conn, cursor)
        
        # push the entries into the table 
        bm_table_accounts.push(t_bm_table_accounts_s._make(args))
        
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def classes(self):
        ''' insert into classes entries
        '''
         
        # push a message to the logger
        self.logger.warn('classes')
         
        # show all classes so far
        menu_print = c_menu_print()
        menu_print.classes()
        
        # we need a generic list in order to fetch the items
        args = []
        
        # loop and fetch the entries
        for item in t_bm_table_classes_s._fields:
            args.append(input("\t\t <--> give us the {}:  ".format(item)))
            if not args[-1]:
                return 0

        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_classes = c_bm_table_classes(conn, cursor)
        
        # push the entries into the table 
        bm_table_classes.push(t_bm_table_classes_s._make(args))
        
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
            for cnt in range(0, len(self.menu_insert)):
                print("{}\t{}".format(self.menu_insert[cnt].get_cmd(), self.menu_insert[cnt].get_help_text()))
             
            c = input("-->")
             
            print(c)
 
            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_insert)):
                if c == self.menu_insert[cnt].cmd:
                    print(self.menu_insert[cnt].get_help_text())
                    self.menu_insert[cnt].fun()
            
            if c =='q':
                break
 
if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()
    