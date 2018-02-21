#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
from bm_globals import *
import mod_logging_mkI_PYTHON
import sqlite3
from collections import namedtuple
from bm_table_accounts import *
from bm_table_class import *
from bm_table_earnings import *
from bm_table_groups_of_expenses import *
from bm_table_groups_of_members import *
from bm_table_invoices import *
from bm_table_matter_of_expenses import *
from bm_table_members import *

''' database definitions
first, there comes a namedtuple in order to ease data retrivals
second, there is a dictionary which holds the data types for each column
'''

class c_bm_database():
    ''' database class
    '''
    def __init__(self):
        self.conn = None
        self.cursor = None
        return
    
    def connect(self):
        '''    connect to the database
        '''
        self.conn = sqlite3.connect("test.db")
        self.cursor = self.conn.cursor()
        return (self.conn, self.cursor)
    
    def disconnect(self):
        ''' disconnect from the database
        '''
        self.cursor.close()
        return 
        
    def manual_db_command(self, _text):
        self.cursor.execute(_text)
        self.conn.commit


class c_app(mod_logging_mkI_PYTHON.c_logging):
    ''' application, does not really do anything
    
    child class of c_logging
    '''
    
    def __init__(self):
        ''' constructor
        '''
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name + ".{}".format(g_program_suffix))
        return
    
    def run(self):
        ''' runs the main 
        '''
        self.logger.debug("application running")
        
        bm_database = c_bm_database()
        (conn, cursor) =  bm_database.connect()
        
        # create and test members
        bm_table_members = c_bm_table_members(conn, cursor)
        bm_table_members._test_routines()

        # create and test matter of expenses
        bm_table_matter_of_expenses = c_bm_table_matter_of_expenses(conn, cursor)
        bm_table_matter_of_expenses._test_routines()

        # disconnect from the database again
        bm_database.disconnect()
    
if __name__ == "__main__":
    # execute only if run as a script
    app = c_app()
    app.run()
