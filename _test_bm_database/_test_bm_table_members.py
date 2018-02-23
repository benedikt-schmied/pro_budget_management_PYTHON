#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_database')

from bm_globals import *
import mod_logging_mkI_PYTHON
from bm_table_members import *
from _test import *

class _test_bm_table_members(c_test_case):

    def __init__(self, _conn, _cursor):
        c_test_case.__init__(self, "table_member", self._test__push_into_members)
        self.conn = _conn
        self.cursor = _cursor

    def _test__push_into_members(self):
        ''' 
        \brief test function for 
        push into members
        '''
        
        # create and test 'members'
        bm_table_members = c_bm_table_members(self.conn, self.cursor)
        bm_table_members._test_routines()
        
        # create a list of members that are to be pushed into the table
        names = ['Horst', 'Hoeness', 'Lolita', 'Kevin']
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if bm_table_members.push(
                t_bm_members_s(
                    name = entry, 
                    group_of_members = 1
                )
            ) != 0:
                return -1
        
        bm_table_members.show_all()
        
        # loop over all entries within the list of names
        for entry in names:
            
            # quit the loop in case of an error
            if bm_table_members.push(
                t_bm_members_s(
                    name = entry, 
                    group_of_members = 1
                )
            ) != -1:
                return -1
        return 0
