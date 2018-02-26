#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_database')
from bm_globals import *
import mod_logging_mkI_PYTHON
from bm_table_invoices import *
from _test import *

class _test_bm_table_invoices(c_test_case):

    def __init__(self, _conn, _cursor):
        
        c_test_case.__init__(self, "invoices", self._test__push_into_invoices)
        self.bm_table_invoices = c_bm_table_invoices(_conn, _cursor)

    def _test__push_into_invoices(self):
        ''' 
        \brief test function for 
        push into matter of expenses
        '''
        self.bm_table_invoices._test_routines()
        
        # create a list of members that are to be pushed into the table
        names = [3, 4, 5, 6]
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if self.bm_table_invoices.push(
                t_bm_table_invoices_s(
                    matter_of_expense = entry, 
                    originator_class = 1, 
                    originator = 1, 
                    date = 1
                    )
            ) != 0:
                return -1
        
        self.bm_table_invoices.show_all()
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if self.bm_table_invoices.push(
                t_bm_table_invoices_s(
                    matter_of_expense = entry, 
                    originator_class = 1, 
                    originator = 1, 
                    date = 1
                    )
            ) != 0:
                return -1
        self.bm_table_invoices.show_all()
        return 0