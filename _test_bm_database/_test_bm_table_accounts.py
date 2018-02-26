#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_database')
from bm_globals import *
import mod_logging_mkI_PYTHON
from bm_table_accounts import *
from _test import *

class _test_bm_table_accounts(c_test_case):

    def __init__(self, _conn, _cursor):
        
        c_test_case.__init__(self, "accounts", self._test__push_into_accounts)
        self.bm_table_accounts = c_bm_table_accounts(_conn, _cursor)

    def _test__push_into_accounts(self):
        ''' 
        \brief test function for 
        push into matter of expenses
        '''
        self.bm_table_accounts._test_routines()
        
        # create a list of expenses that are to be pushed into the table
        names = ['wage01', 'wage02']
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if self.bm_table_accounts.push(
                t_bm_table_accounts_s(
                    name = entry
                    )
            ) != 0:
                return -1
        
        self.bm_table_accounts.show_all()
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if self.bm_table_accounts.push(
                t_bm_table_accounts_s(
                    name = entry
                    )
            ) != 0:
                return -1
        self.bm_table_accounts.show_all()
        return 0