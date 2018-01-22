#!/usr/bin/python3
# coding=latin-1

'''
creation date
author 

objectives:

import and export database entries
'''

import sys
import sqlite3
import os
import argparse
import bm_database
import mod_logging_mkI_PYTHON
from cmdmenu import *

class c_import_export(mod_logging_mkI_PYTHON.c_logging):

    def __init__(self):
        
        mod_logging_mkI_PYTHON.c_logging.__init__(self, "cmd")
        
        # we need a variable which holds the main menu    
        self.menu_top = []
        self.menu_top.append(c_menu_items('i', 'import', 'import a file', self.menu_import))
        self.menu_top.append(c_menu_items('e', 'export', 'export a file', self.menu_export))
        self.menu_top.append(c_menu_items('h', 'help', 'help menu', self.menu_help))
    
    def get_idx_by_cmd(self, _cmd):
        '''
        @param _cmd     command
        '''
        for cnt in range(0, self.menu_top):
            if _cmd == self.menu_top[cnt].cmd:
                return cnt
            return -1
        
    def menu_import(self, _midx):
        '''
        @param _midx    menu index
        '''
        return

    def menu_export(self, _midx):
        '''
        @param _midx:
        '''   
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
    menu = c_import_export()
    menu.run()
