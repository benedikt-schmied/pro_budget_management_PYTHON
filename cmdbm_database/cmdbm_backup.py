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
import zipfile
import time
import collections

class c_backup(mod_logging_mkI_PYTHON.c_logging):

    def __init__(self):
        
        mod_logging_mkI_PYTHON.c_logging.__init__(self, "cmd")
        
        # we need a variable which holds the main menu    
        self.menu_top = []
        self.menu_top.append(c_menu_items('i', 'import', 'import a file', self.menu_import))
        self.menu_top.append(c_menu_items('e', 'export', 'export a file', self.menu_export))
        self.menu_top.append(c_menu_items('t', 'test', 'test routine', self.menu_named))
        self.menu_top.append(c_menu_items('c', 'config', 'configuration files', self.menu_config))
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

    def menu_named(self, _midx):
        '''
        @param _midx     menu index
        '''
        matter_of_expenses = collections.namedtuple('matter_of_expenses', ['name', 'amount', 'account'])
        autokosten = matter_of_expenses(name = 'Autokosten', amount = 6000.0, account = '1')
        versicherung = matter_of_expenses(name = 'Versicherung', amount = 200.0, account = '2')
        print(autokosten)
        print(versicherung)
        print(autokosten.amount + versicherung.amount)
        
        import csv
        
        for entry in map(matter_of_expenses._make, csv.reader(open("bm_matter_of_expense.csv", "rt", encoding='ascii'))):
            print(entry.name, entry.amount)
        return
    
    def menu_config(self, _midx):
        
        import configparser
        config = configparser.ConfigParser()
        
        print(config.sections())
        config.read('example.ini')
        print(config.sections())
        print(type(config))
        test = config['TEST']
        print(type(test))
        print(test['PORT'])
        
        return

    def menu_export(self, _midx):
        '''
        @param _midx:
        '''   
        with zipfile.ZipFile('backup_{}.zip'.format(time.strftime('%Y%m%d%H%M%S')), 'w') as myzip:
            myzip.write('bm_database.db')
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
    menu = c_backup()
    menu.run()
