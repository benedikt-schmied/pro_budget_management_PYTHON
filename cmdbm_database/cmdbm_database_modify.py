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


class c_menu_modify():
    ''' print menu
    '''
     
    def __init__(self):
         
        mod_logging_mkI_PYTHON.c_logging.__init__(self, 'cmd')
         
        # we need a variable which holds the main menu    
        self.menu_modify = []
        self.menu_modify.append(c_menu_items('me', 'members', 'member table', self.members))
        self.menu_modify.append(c_menu_items('ex', 'matter of expense', 'matter of expense', self.matter_of_expenses))  
        self.menu_modify.append(c_menu_items('in', 'invoices', 'invoices', self.invoices))
        self.menu_modify.append(c_menu_items('gm', 'groups of members', 'groups of members', self.groups_of_members))
        self.menu_modify.append(c_menu_items('ge', 'groups of expenses', 'groups of expenses', self.groups_of_expenses))
        self.menu_modify.append(c_menu_items('ea', 'earnings', 'earnings', self.earnings))
        self.menu_modify.append(c_menu_items('ac', 'accounts', 'accounts', self.accounts))
        self.menu_modify.append(c_menu_items('cl', 'classes', 'classes', self.classes))
        return
     
    def members(self):
        ''' insert into members entries
        '''
         
        # push a message to the logger
        self.logger.warn('members')
     
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_members = c_bm_table_members(conn, cursor)
        bm_table_members.show_all_l()
     
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # select the entry
        entries = bm_table_members.select_matching_id(row)
        
        args = []
        args.append(row)
        
        # loop and fetch the entries
        for item in t_bm_table_members_l._fields:
            if item == 'id':
                continue
            args.append(input("\t\t <--> give us the {}: ({}) ".format(item, getattr(entries, item))))
            if not args[-1]:
                args[-1] = getattr(entries, item)
#                                             )
        bm_table_members.update_matching_id(row, t_bm_table_members_l._make(args))
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def matter_of_expenses(self):
        ''' insert into matter_of_expenses entries
        '''
         
        # push a message to the logger
        self.logger.warn('matter_of_expenses')
     
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_matter_of_expenses = c_bm_table_matter_of_expenses(conn, cursor)
        bm_table_matter_of_expenses.show_all_l()
     
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # select the entry
        entries = bm_table_matter_of_expenses.select_matching_id(row)
        
        args = []
        args.append(row)
        
        # loop and fetch the entries
        for item in t_bm_table_matter_of_expenses_l._fields:
            if item == 'id':
                continue
            args.append(input("\t\t <--> give us the {}: ({}) ".format(item, getattr(entries, item))))
            if not args[-1]:
                args[-1] = getattr(entries, item)
#                                             )
        bm_table_matter_of_expenses.update_matching_id(row, t_bm_table_matter_of_expenses_l._make(args))
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def invoices(self):
        ''' insert into invoices entries
        '''
         
        # push a message to the logger
        self.logger.warn('invoices')
     
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_invoices = c_bm_table_invoices(conn, cursor)
        bm_table_invoices.show_all_l()
     
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # select the entry
        entries = bm_table_invoices.select_matching_id(row)
        
        args = []
        args.append(row)
        
        # loop and fetch the entries
        for item in t_bm_table_invoices_l._fields:
            if item == 'id':
                continue
            args.append(input("\t\t <--> give us the {}: ({}) ".format(item, getattr(entries, item))))
            if not args[-1]:
                args[-1] = getattr(entries, item)
#                                             )
        bm_table_invoices.update_matching_id(row, t_bm_table_invoices_l._make(args))
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def groups_of_members(self):
        ''' insert into groups_of_members entries
        '''
         
        # push a message to the logger
        self.logger.warn('groups_of_members')
     
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_groups_of_members = c_bm_table_groups_of_members(conn, cursor)
        bm_table_groups_of_members.show_all_l()
     
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # select the entry
        entries = bm_table_groups_of_members.select_matching_id(row)
        
        args = []
        args.append(row)
        
        # loop and fetch the entries
        for item in t_bm_table_groups_of_members_l._fields:
            if item == 'id':
                continue
            args.append(input("\t\t <--> give us the {}: ({}) ".format(item, getattr(entries, item))))
            if not args[-1]:
                args[-1] = getattr(entries, item)
#                                             )
        bm_table_groups_of_members.update_matching_id(row, t_bm_table_groups_of_members_l._make(args))
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
     
    def groups_of_expenses(self):
        ''' insert into groups_of_expenses entries
        '''
         
        # push a message to the logger
        self.logger.warn('groups_of_expenses')
     
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_groups_of_expenses = c_bm_table_groups_of_expenses(conn, cursor)
        bm_table_groups_of_expenses.show_all_l()
     
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # select the entry
        entries = bm_table_groups_of_expenses.select_matching_id(row)
        
        args = []
        args.append(row)
        
        # loop and fetch the entries
        for item in t_bm_table_groups_of_expenses_l._fields:
            if item == 'id':
                continue
            args.append(input("\t\t <--> give us the {}: ({}) ".format(item, getattr(entries, item))))
            if not args[-1]:
                args[-1] = getattr(entries, item)
#                                             )
        bm_table_groups_of_expenses.update_matching_id(row, t_bm_table_groups_of_expenses_l._make(args))
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def earnings(self):
        ''' insert into earnings entries
        '''
         
        # push a message to the logger
        self.logger.warn('earnings')
     
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_earnings = c_bm_table_earnings(conn, cursor)
        bm_table_earnings.show_all_l()
     
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # select the entry
        entries = bm_table_earnings.select_matching_id(row)
        
        args = []
        args.append(row)
        
        # loop and fetch the entries
        for item in t_bm_table_earnings_l._fields:
            if item == 'id':
                continue
            args.append(input("\t\t <--> give us the {}: ({}) ".format(item, getattr(entries, item))))
            if not args[-1]:
                args[-1] = getattr(entries, item)
#                                             )
        bm_table_earnings.update_matching_id(row, t_bm_table_earnings_l._make(args))
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def accounts(self):
        ''' insert into accounts entries
        '''
         
        # push a message to the logger
        self.logger.warn('accounts')
     
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_accounts = c_bm_table_accounts(conn, cursor)
        bm_table_accounts.show_all_l()
     
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # select the entry
        entries = bm_table_accounts.select_matching_id(row)
        
        args = []
        args.append(row)
        
        # loop and fetch the entries
        for item in t_bm_table_accounts_l._fields:
            if item == 'id':
                continue
            args.append(input("\t\t <--> give us the {}: ({}) ".format(item, getattr(entries, item))))
            if not args[-1]:
                args[-1] = getattr(entries, item)
#                                             )
        bm_table_accounts.update_matching_id(row, t_bm_table_accounts_l._make(args))
         
        # now, disconnect again
        bm_database.disconnect()
        return
     
    def classes(self):
        ''' insert into classes entries
        '''
         
        # push a message to the logger
        self.logger.warn('classes')
     
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_classes = c_bm_table_classes(conn, cursor)
        bm_table_classes.show_all_l()
     
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # select the entry
        entries = bm_table_classes.select_matching_id(row)
        
        args = []
        args.append(row)
        
        # loop and fetch the entries
        for item in t_bm_table_classes_l._fields:
            if item == 'id':
                continue
            args.append(input("\t\t <--> give us the {}: ({}) ".format(item, getattr(entries, item))))
            if not args[-1]:
                args[-1] = getattr(entries, item)
#                                             )
        bm_table_classes.update_matching_id(row, t_bm_table_classes_l._make(args))
         
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
            for cnt in range(0, len(self.menu_modify)):
                print("{}\t{}".format(self.menu_modify[cnt].get_cmd(), self.menu_modify[cnt].get_help_text()))
             
            c = input("-->")
             
            print(c)
 
            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_modify)):
                if c == self.menu_modify[cnt].cmd:
                    print(self.menu_modify[cnt].get_help_text())
                    self.menu_modify[cnt].fun()
            
            if c =='q':
                break
             
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