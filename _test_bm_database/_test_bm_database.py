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

    print(bm_database.get_entries_members(c))
    
    if bm_database.select_from_members_where_name_match(c, "Horst") != 1:
        return -1
    
    cnti = 2
    for entry in names:
        if bm_database.select_from_members_where_name_match(c, entry) != cnti:
            return -1
        cnti = cnti + 1



    # destroy all entries in oder to run clean upcoming tests
    bm_database.pop_all_from_members(c)


    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_members(c)
    

    
    
    # disconnect from the base  
    bm_database.disconnect(c)
    
    return 0

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

def _test__push_into_invoice():
    ''' 
    \brief test function for 
    push into matter of expenses
    '''
   
    # connect to the database 
    c=bm_database.connect()
    
    # setup the database
    bm_database.setup_db(c)
    
    # use for - statement to loop upon the test cases
    if bm_database.push_into_invoice(c, 1, 1, "25.Mai 2017") != 0:
        return -1
    
    names = ['Hoeness', 'Lolita', 'Kevin']
    for entry in names:
        print(entry)
        if bm_database.push_into_invoice(c, 1, 1, "25.Mai 2017") != 0:
            break
    
    bm_database.show_all_invoices(c)
    
    if bm_database.select_from_invoices_where_matter_of_expense_match(c, 1) != 1:
        return -1
    else:
        print("we've found it")
        
    # destroy all entries in oder to run clean upcoming tests
    bm_database.pop_all_from_invoices(c)

    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_invoices(c)
    
    # disconnect from the base  
    bm_database.disconnect(c)
    
    return 0

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
    # destroy all entries in oder to run clean upcoming tests
    bm_database.pop_all_from_accounts(c)

    print("now showing all members")

    # check, whether there are still entries within this database
    bm_database.show_all_accounts(c)
    
    # disconnect from the base  
    bm_database.disconnect(c)
    return 0

def main():
    '''
    \brief main routine
    \param void
    '''
    d=[]
    d.append(c_test_case(_test__push_into_members))
    d.append(c_test_case(_test__push_into_matter_of_expenses))
    d.append(c_test_case(_test__push_into_invoice))
    d.append(c_test_case(_test__push_into_groups_of_expenses))
    d.append(c_test_case(_test__push_into_earnings))
    d.append(c_test_case(_test__push_into_accounts))
    for cnti in range(0, len(d)):
        if (d[cnti].fun() != 0):
            print("test ", cnti, " failed")
            return
    print("all tests successful")

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
    main()