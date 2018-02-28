#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_database')
from bm_globals import *
import mod_logging_mkI_PYTHON
from bm_table_classes import *
from _test import *

class _test_bm_table_classes(c_test_case):

    def __init__(self, _conn, _cursor):
        
        c_test_case.__init__(self, "classes", self._test__push_into_classes)
        self.bm_table_classes = c_bm_table_classes(_conn, _cursor)

    def _test__push_into_classes(self):
        ''' 
        \brief test function for 
        push into matter of expenses
        '''
        self.bm_table_classes._test_routines()
        
        # create a list of expenses that are to be pushed into the table
        names = ['wage01', 'wage02']
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if self.bm_table_classes.push(
                t_bm_table_classes_s(
                    name = entry
                    )
            ) != 0:
                return -1
        
        self.bm_table_classes.show_all()
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if self.bm_table_classes.push(
                t_bm_table_classes_s(
                    name = entry
                    )
            ) != 0:
                return -1
        self.bm_table_classes.show_all()
        return 0