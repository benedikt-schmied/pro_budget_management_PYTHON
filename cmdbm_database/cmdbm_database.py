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
from cmdbm_database_calc import *
from cmdbm_database_delete import *
from cmdbm_database_insert import *
from cmdbm_database_modify import *
from cmdbm_database_print import *
from cmdbm_database_setup import *
from cmdbm_database_export import *


class c_menu_help():
    ''' help menu
    '''
    
    def __init__(self):
        return
    
    def run(self):
        return

class c_menu_top(mod_logging_mkI_PYTHON.c_logging):

    def __init__(self):
        
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name)
        
        # we need a variable which holds the main menu    
        self.menu_top = []
        self.menu_top.append(c_menu_items('s', 'setup', 'setup the database', self.menu_setup))
        self.menu_top.append(c_menu_items('p', 'print', 'printing something', self.menu_print))
        self.menu_top.append(c_menu_items('m', 'modify', 'modify an entry', self.menu_modify))
        self.menu_top.append(c_menu_items('i', 'insert', 'insert an entry', self.menu_insert))
        self.menu_top.append(c_menu_items('d', 'delete', 'delete an entry', self.menu_delete))
        self.menu_top.append(c_menu_items('c', 'calc', 'do some calculation', self.menu_calc))
        self.menu_top.append(c_menu_items('e', 'export', 'export', self.menu_export))
        self.menu_top.append(c_menu_items('m', 'manual', 'manual', self.menu_manual))
        self.menu_top.append(c_menu_items('h', 'help', 'help menu', self.menu_help))
    
    def get_idx_by_cmd(self, _cmd):
        '''
        @param _cmd     command
        '''
        for cnt in range(0, self.menu_top):
            if _cmd == self.menu_top[cnt].cmd:
                return cnt
            return -1
        
    def menu_setup(self, _midx):
        '''
        @param _midx    menu index
        '''
        menu_setup = c_menu_setup()
        menu_setup.run()
        
    def menu_print(self, _midx):
        '''
        @param _midx    menu index
        '''
        menu_print = c_menu_print()
        menu_print.run()
        
    def menu_modify(self, _midx):
        '''
        @param _midx:
        '''    
        menu_modify = c_menu_modify()
        menu_modify.run()
        
    def menu_insert(self, _midx):
        '''
        @param _midx:
        '''
        menu_insert = c_menu_insert()
        menu_insert.run()

    def menu_delete(self, _midx):
        '''
        @param _midx:
        '''
        menu_delete = c_menu_delete()
        menu_delete.run()

    def menu_calc(self, _midx):
        '''
        @param _midx:
        '''
        menu_calc = c_menu_calc()
        menu_calc.run()

    def menu_export(self, _midx):
        '''
        @param _midx:
        '''
        menu_export = c_menu_export()
        menu_export.run()

    def menu_manual(self, _midx):
        '''
        @param _midx:
        '''
        
#         d = bm_database.connect()
#         stmt = input("\t\t <--> typ the command: ")
#         bm_database.manual_db_command(d, stmt)
#         bm_database.disconnect(d)
        return
    
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
            
            for cnt in range(0, len(self.menu_top)):
                print("{}\t{}".format(self.menu_top[cnt].get_cmd(), self.menu_top[cnt].get_help_text()))
            
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