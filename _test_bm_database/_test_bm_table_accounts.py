#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_database')

from bm_globals import *
import mod_logging_mkI_PYTHON
from bm_table_accounts import *

def _test__push_into_accounts():
    ''' 
    \brief test function for 
    push into matter of expenses
    '''
   
    # connect to the database 
    c=bm_database.connect()
    
    # setup the database
    bm_database.setup_db(c)
    
    # use for - statement to loop upon the test cases
    if bm_database.push_into_accounts(c, "Giro Horst") != 0:
        return -1
    
    names = ['Tagesgeld Hoeness', 'Giro Haushalt', 'Tagesgeld Lolita']
    for entry in names:
        print(entry)
        if bm_database.push_into_accounts(c, entry) != 0:
            break
    
    bm_database.show_all_accounts(c)
        
    if (bm_database.select_from_accounts_where_name_match(c, "Giro Horst") != 1):
        return -1
    else:
        print("found an entry")
    
    bm_database.disconnect(c)
    
    c = bm_database.connect()

    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_accounts(c)
    
    # disconnect from the base  
    bm_database.disconnect(c)
    
    c = bm_database.connect()
    
    # destroy all entries in oder to run clean upcoming tests
    bm_database.pop_all_from_accounts(c)

    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_accounts(c)
    
    # disconnect from the base  
    bm_database.disconnect(c)
    
    c = bm_database.connect()

    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_accounts(c)
    
    # disconnect from the base  
    bm_database.disconnect(c)
    
    return 0