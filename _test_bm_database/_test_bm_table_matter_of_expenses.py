#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_database')
from bm_globals import *
import mod_logging_mkI_PYTHON
from bm_table_matter_of_expenses import *
from _test import *

class _test_bm_table_matter_of_expenses(c_test_case):

    def __init__(self, _conn, _cursor):
        
        c_test_case.__init__(self, "matter_of_expenses", self._test__push_into_matter_of_expenses)
        self.bm_table_matter_of_expense = c_bm_table_matter_of_expenses(_conn, _cursor)

    def _test__push_into_matter_of_expenses(self):
        ''' 
        \brief test function for 
        push into matter of expenses
        '''
        self.bm_table_matter_of_expense._test_routines()
        
        # create a list of members that are to be pushed into the table
        names = ['Frisör', 'Autoversicherung', 'Essen', 'Trinken']
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if self.bm_table_matter_of_expense.push(
                t_bm_table_matter_of_expenses_s(
                    name = entry, 
                    originator = 1, 
                    originator_class = 1, 
                    provider = 1, 
                    provider_class = 1,
                    groups_of_expenses = 1, 
                    amount = 1.4, 
                    frequency = 1, 
                    account = 1)
            ) != 0:
                return -1
        
        self.bm_table_matter_of_expense.show_all()
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if self.bm_table_matter_of_expense.push(
                t_bm_table_matter_of_expenses_s(
                    name = entry, 
                    originator = 1, 
                    originator_class = 1, 
                    provider = 1, 
                    provider_class = 1,
                    groups_of_expenses = 1, 
                    amount = 1.4, 
                    frequency = 1, 
                    account = 1)
            ) != 0:
                return -1
        self.bm_table_matter_of_expense.show_all()
        return 0