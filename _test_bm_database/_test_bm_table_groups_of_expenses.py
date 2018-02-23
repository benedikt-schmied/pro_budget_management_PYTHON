#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_table_groups_of_expenses')

from bm_globals import *
import mod_logging_mkI_PYTHON
from bm_table_groups_of_expenses import *

def _test__push_into_groups_of_expenses():
    ''' 
    \brief test function for 
    push into matter of expenses
    '''
   
    # connect to the database 
    c=bm_database.connect()
    
    # setup the database
    bm_database.setup_db(c)
    
    # use for - statement to loop upon the test cases
    if bm_database.push_into_groups_of_expenses(c, "Familie") != 0:
        return -1
    
    names = ['Hoeness', 'Haushalt', 'Auto']
    for entry in names:
        print(entry)
        if bm_database.push_into_groups_of_expenses(c, entry) != 0:
            break
    
    bm_database.show_all_groups_of_expenses(c)
    
    if bm_database.select_from_groups_of_expense_where_name_match(c, "Familie") != 1:
        return -1
        
    # destroy all entries in oder to run clean upcoming tests
    bm_database.pop_all_from_groups_of_expenses(c)

    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_groups_of_expenses(c)
    
    # disconnect from the base  
    bm_database.disconnect(c)
    return 0

