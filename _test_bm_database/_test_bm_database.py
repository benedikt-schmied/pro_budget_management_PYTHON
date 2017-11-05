#!/usr/bin/python3
# coding=latin-1

import sys
import sqlite3
import os
import bm_database
from enum import Enum

class test_result(Enum):
    failed = -1
    succeeded = 0

class c_test_case():
    ''' 
    \brief test case class
    '''
    
    def __init__(self, _fun):
        ''' the constructor
        '''
        self.fun = _fun # function

def test_assert(_expected, _actual):
    ''' assert statement
    '''
    if (_expected != _actual):
        return

def _test__push_into_members():
    ''' 
    \brief test function for 
    push into members
    '''
   
    # connect to the database 
    c=bm_database.connect()
    
    # setup the database
    bm_database.setup_db(c)
    
    # use for - statement to loop upon the test cases
    if bm_database.push_into_members(c, "Horst", 1) != 0:
        return -1
    
    if bm_database.push_into_members(c, "Horst", 1) != -1:
        return -1
    
    names = ['Hoeness', 'Lolita', 'Kevin']
    for entry in names:
        print(entry)
        if bm_database.push_into_members(c, entry, 1) != 0:
            break
    
    bm_database.show_all_members(c)
        
    # destroy all entries in oder to run clean upcoming tests
    bm_database.pop_all_from_members(c)

    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_members(c)
    
    # disconnect from the base  
    bm_database.disconnect(c)

def main():
    '''
    \brief main routine
    \param void
    '''

    d = c_test_case(_test__push_into_members)
    d.fun()
        


if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
    main()