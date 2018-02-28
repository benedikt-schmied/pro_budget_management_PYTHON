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
        self.menu_insert.append(c_menu_items('ex', 'matter of expense', 'matter of expense', self.matter_of_expense))  
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
         
        # ask the user for specific inputs        
        name = input("\t\t <--> name: ")

        # show all members so far
        menu_print.groups_of_members()
         
        # ask the user for specific inputs        
        group_of_members = input("\t\t <--> groups_of_members: ")

        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_members = c_bm_table_members(conn, cursor)
        
        # create a variable which holds the entries
        test = t_bm_table_members_s(name = name, 
                                    group_of_members = group_of_members)
         
        bm_table_members.push(test)
        # now, disconnect again
        bm_database.disconnect()
        return
#     
    def matter_of_expense(self):
        ''' insert into matter of expense
         
        '''
         
        # push a message to the logger
        self.logger.warn('matter of expense')
 
        # print all existing entries
        menu_print = c_menu_print()
        menu_print.matter_of_expense()
 
        # ask the user for specific iputs
        name = input("\t\t <--> name: ")
         
        # print the members table in order to help the user
        menu_print.classes()
        menu_print.members()
        menu_print.groups_of_members()
         
        originator_class = input("\t\t <--> originator class: ")
        originator = input("\t\t <--> originator: ")
        provider_class = input("\t\t <--> provider class: ")
        provider = input("\t\t <--> provider: ")
         
        # print the groups of expenses table
        menu_print.groups_of_expenses()
        group = input("\t\t <--> group: ")
        amount = input("\t\t <--> amount: ")
         
        # tell the user to give the frequency in weeks
        frequency = input("\t\t <--> frequency [weeks]: ")
         
        # print the accounts table
        menu_print.accounts()
        account = input("\t\t <--> account: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_matter_of_expenses = c_bm_table_matter_of_expenses(conn, cursor)
        
        # create a variable which holds the entries
        test = t_bm_table_matter_of_expenses_s(
                    name = name, 
                    originator = originator, 
                    originator_class = originator_class, 
                    provider = provider, 
                    provider_class = provider_class,
                    groups_of_expenses = group, 
                    amount = amount, 
                    frequency = frequency, 
                    account = account)
         
        bm_table_matter_of_expenses.push(test)
        
        # now, disconnect again
        bm_database.disconnect()
        return
#     
    def invoices(self):
        ''' insert into the invoices table
        '''
         
        # push a message into the logger
        self.logger.warn('matter of invoices')
     
        # ask the user for specific inputs    
        matter_of_expense = input("\t\t <--> matter of expense: ")
        originator = input("\t\t <--> originator: ")
        date = input("\t\t <--> date: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
         
        test = t_bm_table_invoices_s(
                    matter_of_expense = matter_of_expense, 
                    originator_class = originator, 
                    originator = originator, 
                    date = date
                    )
        
        # now, push it to the table
        bm_table_invoices = c_bm_table_invoices(conn, cursor)
         
        bm_table_invoices.push(test)
        
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def groups_of_members(self):
        ''' insert into the group of members table
        '''
         
        # push a message into the logger
        self.logger.warn('groups of members')
 
        # print the members table in order to help the user
        menu_print = c_menu_print()
        menu_print.groups_of_members()
 
        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
         
        test = t_bm_table_groups_of_members_s(
                    name = name
                    )
        
        # now, push it to the table
        bm_table_groups_of_members = c_bm_table_groups_of_members(conn, cursor)
         
        bm_table_groups_of_members.push(test)
        
        # now, disconnect again
        bm_database.disconnect()
        return   
     
     
    def groups_of_expenses(self):
        ''' insert into the group of expenses tables
        '''
         
        # push a message into the logger
        self.logger.warn('groups of expenses')
 
                # print the members table in order to help the user
        menu_print = c_menu_print()
        menu_print.groups_of_expenses()
 
        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
         
        test = t_bm_table_groups_of_expenses_s(
                    name = name
                    )
        
        # now, push it to the table
        bm_table_groups_of_expenses = c_bm_table_groups_of_expenses(conn, cursor)
         
        bm_table_groups_of_expenses.push(test)
        
        # now, disconnect again
        bm_database.disconnect()
        return 
     
    def earnings(self):
        ''' print the earnings entries
        '''
         
        # push a message into the logger
        self.logger.warn('earnings')
 
        # print the members table in order to help the user
        menu_print = c_menu_print()
        menu_print.earnings()
 
        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
         
        # print the members table in order to help the user
        menu_print.accounts()
         
        account = input("\t\t <--> account: ")
        amount = input("\t\t <--> amount: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
         
        test = t_bm_table_earnings_s(
                    name = name, 
                    account = account, 
                    amount = amount
                    )
        
        # now, push it to the table
        bm_table_earnings = c_bm_table_earnings(conn, cursor)
         
        bm_table_earnings.push(test)
        
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def accounts(self):
        ''' print the accounts entries
        '''
         
        # push a message into the logger
        self.logger.warn('accounts')
 
        # print the members table in order to help the user
        menu_print = c_menu_print()
        menu_print.accounts()
 
        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
         
        test = t_bm_table_accounts_s(
                    name = name
                    )
        
        # now, push it to the table
        bm_table_accounts = c_bm_table_accounts(conn, cursor)
         
        bm_table_accounts.push(test)
        
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def classes(self):
        ''' print the classes entries
        '''
         
        # push a message into the logger
        self.logger.warn('classes')
 
        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
         
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
         
        test = t_bm_table_classes_s(
                    name = name
                    )
        
        # now, push it to the table
        bm_table_classes = c_bm_table_classes(conn, cursor)
         
        bm_table_classes.push(test)
        
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
    