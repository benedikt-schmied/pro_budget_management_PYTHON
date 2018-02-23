#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_database')
from bm_globals import *
import mod_logging_mkI_PYTHON
from bm_table_matter_of_expenses import *

def _test__push_into_matter_of_expenses():
    ''' 
    \brief test function for 
    push into matter of expenses
    '''
   
    # connect to the database 
    c=bm_database.connect()
    
    # setup the database
    bm_database.setup_db(c)
    
    # use for - statement to loop upon the test cases
    if bm_database.push_into_matter_of_expense(c, "Frisoer Benedikt", 1, 1, 1, 20, "monthly", 1) != 0:
        return -1
    
    names = ['Hoeness', 'Lolita', 'Kevin']
    for entry in names:
        print(entry)
        if bm_database.push_into_matter_of_expense(c, "Frisoer " + entry, 1, 1, 1, 20, "monthly", 1) != 0:
            break
    
    bm_database.show_all_matter_of_expense(c)
    
    if bm_database.select_from_matter_of_expense_where_name_match(c, "Frisoer Benedikt") != 1:
        return -1
    else:
        print("we've found an entry")
    
        
    # destroy all entries in oder to run clean upcoming tests
    bm_database.pop_all_from_matter_of_expense(c)

    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_matter_of_expense(c)
    
    # disconnect from the base  
    bm_database.disconnect(c)
    
    # now, we connect again, and try to push these entries again
    c = bm_database.connect()
    
    bm_database.show_all_matter_of_expense(c)
    
    names = ['Hoeness', 'Lolita', 'Kevin']
    for entry in names:
        print(entry)
        if bm_database.push_into_matter_of_expense(c, "Frisoer " + entry, 1, 1, 1, 20, "monthly", 1) != 0:
            break
    
    bm_database.show_all_matter_of_expense(c)
    
    bm_database.disconnect(c)
    
    print("reopen it again")
    
    c = bm_database.connect()
    
    bm_database.show_all_matter_of_expense(c)
    
    bm_database.disconnect(c)
    
    
    
    
    return 0