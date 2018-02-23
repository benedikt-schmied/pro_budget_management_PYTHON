#!/usr/bin/python3
# coding=latin-1

import sys
from _test_bm_table_members import _test_bm_table_members


sys.path.append('../bm_database')
sys.path.append('../mod_logging_mkI_PYTHON')
sys.path.append('../_pro')

import mod_logging_mkI_PYTHON
from bm_database import *
from _test_bm_table_members import *
from bm_globals import *


class c_app(mod_logging_mkI_PYTHON.c_logging):
    ''' 
    
    child of mod_logging_mkI_PYTHON 
    '''
    
    def __init__(self):
        ''' constructor which configures the logging library
        '''
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name)
        
        self.bm_database = c_bm_database()
        (self.conn, self.cursor) =  self.bm_database.connect()
        
        self.test = c_test()
        self.test.append(_test_bm_table_members(self.conn, self.cursor))
        
    def run(self):
        '''
        '''
        self.test.run()

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
    app = c_app()
    app.run()