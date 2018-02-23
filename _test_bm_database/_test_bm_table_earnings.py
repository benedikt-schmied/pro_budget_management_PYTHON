#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_database')

from bm_globals import *
import mod_logging_mkI_PYTHON
from bm_table_earnings import *

def _test__push_into_earnings():
    ''' 
    \brief test function for 
    push into matter of expenses
    '''
   
    # connect to the database 
    c=bm_database.connect()
    
    # setup the database
    bm_database.setup_db(c)
    
    # use for - statement to loop upon the test cases
    if bm_database.push_into_earnings(c, "Giro Horst", 1, 2500) != 0:
        return -1
    
    names = ['Tagesgeld Hoeness', 'Giro Haushalt', 'Tagesgeld Lolita']
    for entry in names:
        print(entry)
        if bm_database.push_into_earnings(c, entry, 1, 2500) != 0:
            break
    
    bm_database.show_all_earnings(c)
        
    if (bm_database.select_from_earnings_where_name_match(c, "Giro Horst") != 1):
        return -1
    # destroy all entries in oder to run clean upcoming tests
    bm_database.pop_all_from_earnings(c)

    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_earnings(c)
    
    # disconnect from the base  
    bm_database.disconnect(c)
    return 0


