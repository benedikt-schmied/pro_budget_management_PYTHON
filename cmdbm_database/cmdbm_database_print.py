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


class c_menu_print(mod_logging_mkI_PYTHON.c_logging):
    ''' print menu
    '''
    
    def __init__(self):
        
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name + ".print")
        
        # we need a variable which holds the main menu    
        self.menu_print = []
        self.menu_print.append(c_menu_items('at', 'all tables', 'print all tables', self.all_tables))
        self.menu_print.append(c_menu_items('me', 'members', 'print the member table', self.members))
        self.menu_print.append(c_menu_items('ex', 'matter of expense', 'matter of expense', self.matter_of_expense))  
        self.menu_print.append(c_menu_items('in', 'invoices', 'invoices', self.invoices))
        self.menu_print.append(c_menu_items('gm', 'groups of members', 'groups of members', self.groups_of_members))
        self.menu_print.append(c_menu_items('ge', 'groups of expenses', 'groups of expenses', self.groups_of_expenses))
        self.menu_print.append(c_menu_items('ea', 'earnings', 'earnings', self.earnings))
        self.menu_print.append(c_menu_items('ac', 'accounts', 'accounts', self.accounts))
        self.menu_print.append(c_menu_items('cl', 'classes', 'classes', self.classes))
        return
    
    def all_tables(self):
        self.logger.warn('all tables')
        self.members()
        self.matter_of_expense()
        self.invoices()
        self.groups_of_members()
        self.groups_of_expenses()
        self.earnings()
        self.accounts()
        self.classes()
        return
    
    def members(self):
        ''' print the members entries
        '''
        
        # push a message to the logger
        self.logger.warn('members')
        
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_members = c_bm_table_members(conn, cursor)
        
        # fetch the entries
        
        # show an introduction line
        print("\t\t ~~~ members")
        
        bm_table_members.show_all()

        # disconnect again
        bm_database.disconnect()
        return 
    
    def matter_of_expense(self):
        ''' print the matter of expense entries
        
        '''
        
        # push a message to the logger
        self.logger.warn('matter of expenses')
        
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_matter_of_expenses = c_bm_table_matter_of_expenses(conn, cursor)
        
        # show an introduction line
        print("\t\t ~~~ members")
        
        bm_table_matter_of_expenses.show_all()
        

        bm_database.disconnect()
        return
    
    def invoices(self):
        ''' print the invoices entries
        '''
        
        # push a message into the logger
        self.logger.warn('invoices')
        
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_invoices = c_bm_table_invoices(conn, cursor)
        
        # fetch the entries
        entries = bm_table_invoices.get_all()
        
        # show an introduction line
        print("\t\t ~~~ invoices")
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, name = \t{}".format(cnti[0], cnti[1]))

        # disconnect again
        bm_database.disconnect()
        return 
    
    def groups_of_members(self):
        ''' print the group of members entries
        '''
        
        # push a message into the logger
        self.logger.warn('groups of members')
        
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_groups_of_members = c_bm_table_groups_of_members(conn, cursor)
        
        # fetch the entries
        entries = bm_table_groups_of_members.get_all()
        
        # show an introduction line
        print("\t\t ~~~ groups of members")
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, name = {}".format(cnti[0], cnti[1]))

        # disconnect again
        bm_database.disconnect()
        return    
    
    
    def groups_of_expenses(self):
        ''' print the group of expenses entries
        '''
        
        # push a message into the logger
        self.logger.warn('groups of expenses')
        
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_groups_of_expenses = c_bm_table_groups_of_expenses(conn, cursor)
        
        # fetch the entries
        entries = bm_table_groups_of_expenses.get_all()
        
        # show an introduction line
        print("\t\t ~~~ groups of expenses")
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> index = {}, name = {}".format(cnti[0], cnti[1]))

        # disconnect again
        bm_database.disconnect()
        return
    
    def earnings(self):
        ''' print the earnings entries
        '''
        
        # push a message into the logger
        self.logger.warn('earnings')
        
                # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_earnings = c_bm_table_earnings(conn, cursor)
        
        # fetch the entries
        entries = bm_table_earnings.get_all()
        
        # show an introduction line
        print("\t\t ~~~ earnings")
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, name = {}, account = {}, amount = {}".format(cnti[0], cnti[1], cnti[2], cnti[3]))

        # disconnect again
        bm_database.disconnect()
        return
    
    def accounts(self):
        ''' print the accounts entries
        '''
        
        # push a message into the logger
        self.logger.warn('accounts')
        
                # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_accounts = c_bm_table_accounts(conn, cursor)
        
        # fetch the entries
        entries = bm_table_accounts.get_all()
        
        # show an introduction line
        print("\t\t ~~~ accounts")        
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, account = {}".format(cnti[0], cnti[1]))

        # disconnect again
        bm_database.disconnect()
        return
    
    def classes(self):
        ''' print the classes entries
        '''
        
        # push a message into the logger
        self.logger.warn('classes')
        
                # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()

        # create a member class
        bm_table_classes = c_bm_table_classes(conn, cursor)
        
        # fetch the entries
        entries = bm_table_classes.get_all()
        
        # show an introduction line
        print("\t\t ~~~ classes")        
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, account = {}".format(cnti[0], cnti[1]))

        # disconnect again
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
            for cnt in range(0, len(self.menu_print)):
                print("{}\t{}".format(self.menu_print[cnt].get_cmd(), self.menu_print[cnt].get_help_text()))
            
            c = input("-->")
            
            print(c)

            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_print)):
                if c == self.menu_print[cnt].cmd:
                    print(self.menu_print[cnt].get_help_text())
                    self.menu_print[cnt].fun()
           
            if c =='q':
                break
    
if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()