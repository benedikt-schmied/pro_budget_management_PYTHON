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
import mod_logging_mkI_PYTHON

class c_menu_items():
    
    def __init__(self, _cmd = "n", _name = "none", _text = "no text", _fun = quit):
        self.cmd = _cmd
        self.name = _name
        self.help_text = _text
        self.fun = _fun    
        
    def set_function(self, _fun):
        self.fun = _fun
        
    def get_function(self):
        return self.fun
    
    def set_help_text(self, _text):
        self.help_text = _text
        
    def get_help_text(self):
        return self.help_text
    
    def set_name(self, _name):
        self.name = _name
        
    def get_name(self):
        return self.name
    
    def set_cmd(self, _cmd):
        self.cmd = _cmd
        
    def get_cmd(self):
        return self.cmd
    
class c_menu_help():
    ''' help menu
    '''
    
    def __init__(self):
        return
    
    def run(self):
        return

class c_menu_print():
    ''' print menu
    '''
    
    def __init__(self):
        
                # we need a variable which holds the main menu    
        self.menu_top = []
        self.menu_top.append(c_menu_items('at', 'all tables', 'print all tables', self.all_tables))
        self.menu_top.append(c_menu_items('me', 'members', 'print the member table', self.members))
        self.menu_top.append(c_menu_items('ex', 'matter of expense', 'matter of expense', self.matter_of_expense))  
        self.menu_top.append(c_menu_items('in', 'invoices', 'invoices', self.invoices))
        self.menu_top.append(c_menu_items('gm', 'groups of members', 'invoices', self.members))
        self.menu_top.append(c_menu_items('ge', 'groups of expenses', self.expenses))
        self.menu_top.append(c_menu_items('ea', 'earnings', 'earnings', self.earnings))
        self.menu_top.append(c_menu_items('ac', 'accounts', 'accounts', self.accounts))
        
        return
    
    def all_tables(self):
        return
    
    def matter_of_expense(self):
        return
    
    def members(self):
        return
    
    def invoices(self):
        return 
    
    def run(self):
        
        '''
        this is the main menu, you can either tell us to 
        print a table
        insert a new entry into a table
        or modify an entry within a table
        '''    
        
        while True:
            
            c = input("-->")
            
            print(c)
            
            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_top)):
                if c == self.menu_top[cnt].cmd:
                    print(self.menu_top[cnt].get_help_text())
                    self.menu_top[cnt].fun(cnt)
           
            if c =='q':
                break
    
    
    
class c_men_insert():
    ''' insert menu
    '''
    
    def __init__(self):
        return
    
    def run(self):
        return
    
    
class c_menu_top():

    def __init__(self):
        print("starting the menu")
        
        # we need a variable which holds the main menu    
        self.menu_top = []
        self.menu_top.append(c_menu_items('p', 'print', 'printing something', self.menu_print))
        self.menu_top.append(c_menu_items('m', 'modify', 'modify an entry', self.menu_modify))
        self.menu_top.append(c_menu_items('i', 'insert', 'insert an entry', self.menu_insert))  
        self.menu_top.append(c_menu_items('h', 'help', 'help menu', self.menu_help))
    
    def get_idx_by_cmd(self, _cmd):
        '''
        @param _cmd     command
        '''
        for cnt in range(0, self.menu_top):
            if _cmd == self.menu_top[cnt].cmd:
                return cnt
            return -1
        
    def menu_print(self, _midx):
        '''
        @param _midx    menu index
        '''
        
        d = bm_database.connect()

        entries = bm_database.get_entries_matter_of_expense(d)
        
        # run over all entries
        for cnti in entries:
            print(cnti)
            
        bm_database.show_all_matter_of_expense(d)
        bm_database.disconnect(d) 

    
    def menu_modify(self, _midx):
        '''
        @param _midx:
        '''    
        
    def menu_insert(self, _midx):
        '''
        @param _midx:
        '''  
        
        d = bm_database.connect()
        bm_database.setup_db(d)
        name = input("-- name: ")
        value = input("-- value: ")
        
        bm_database.push_into_matter_of_expense(d, name, value, 1, 1, 20, "monthly", 1)
        bm_database.disconnect(d)
    
    def menu_help(self, _midx):
        '''
        @param 
        ''' 
        for item in self.menu_top:
            print("cmd ", item.get_cmd(), "\t", item.get_help_text())
    
    def run(self):
        '''
        @param _midx:
        '''  
        
        '''
        this is the main menu, you can either tell us to 
        print a table
        insert a new entry into a table
        or modify an entry within a table
        '''    
        
        while True:
            
            c = input("-->")
            
            print(c)
            
            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_top)):
                if c == self.menu_top[cnt].cmd:
                    print(self.menu_top[cnt].get_help_text())
                    self.menu_top[cnt].fun(cnt)
           
            if c =='q':
                break
                

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()
    menu = c_menu_top()
    menu.run()