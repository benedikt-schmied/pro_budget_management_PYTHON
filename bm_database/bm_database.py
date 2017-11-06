#!/usr/bin/python3 
# coding=latin-1
import sys
import sqlite3
import os

def main():
    ''' 
    \brief main routine
    \return void
    '''
    c= connect()
    setup_db(c)
    disconnect(c)

def connect():
    ''' 
    \brief connect to the database
    '''
    conn = sqlite3.connect("budget_management.db")
    c = conn.cursor()
    return c

def disconnect(_cursor):
    ''' 
    \brief disconnect from the database
    '''
    _cursor.close()

def setup_db(_cursor):
    ''' 
    \brief setup the database
    
    \param _cursor    database cursor
    '''
    print("setting up the database as well as the tables")
   
    for i in range(0,7):
        try:
            if i == 0:
                _cursor.execute("CREATE TABLE members (id integer primary key, name text unique, group_of_members integer)")
            elif i == 1:
                _cursor.execute("CREATE TABLE matter_of_expense (id integer primary key, name text, originator integer, provider name, group_of_expenses integer, amount float, account integer)")
            elif i == 2:
                _cursor.execute("CREATE TABLE invoices (id integer primary key, matter_of_expense integer, integer originator, date text)")
            elif i == 3:
                _cursor.execute("CREATE TABLE groups_of_expenses (id integer primary key, name text unique)")
            elif i == 4:
                _cursor.execute("CREATE TABLE groups_of_members (id integer primary key, name text unique)")
            elif i == 5:
                _cursor.execute("CREATE TABLE earnings (id integer primary key, name text unique, account integer, amount integer)")    
            elif i == 6:
                _cursor.execute("CREATE TABLE accounts (id integer primary key, name text unique)")    
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
    return _cursor

def destroy_db(_cursor):
    '''
    \brief destroy the database again
    
    \param _cursor    database cursor
    '''
    
    print("dstroying the database which includes the tables")
    
    for i in [6,5,4,3,2,1,0]:
        try:
            if i == 0:
                _cursor.execute("DROP TABLE members")
            elif i == 1:
                _cursor.execute("DROP TABLE matter_of_expense")
            elif i == 2:
                _cursor.execute("DROP TABLE invoices")
            elif i == 3:
                _cursor.execute("DROP TABLE groups_of_expenses")
            elif i == 4:
                _cursor.execute("DROP TABLE groups_of_members")
            elif i == 5:
                _cursor.execute("DROP TABLE earnings")    
            elif i == 6:
                _cursor.execute("DROP TABLE accounts")    
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
    return _cursor
    

def push_into_members(_cursor, _name, _group):
    ''' 
    \brief pushes a new entry into 'members' table
    
    \param _cursor   database cursor
    \param _name     member's name
    \param _group    member's group ID
    '''
    print("    pushing member")
    try:
        _cursor.execute("INSERT INTO members(name, group_of_members) values (?,?)", (_name, _group,))
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1                 

def pop_from_members(_cursor, _name):
    ''' 
    \brief pops a new entry into 'members' table
    
    \param _cursor   database cursor
    \param _name     member's name
    \param _group    member's group ID
    '''
    print("    pop from member")
    try:
        _cursor.execute("DELETE FROM members WHERE name=?", (_name,))
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1

def pop_all_from_members(_cursor):
    '''
    \brief pop all entries from the 'member' table
    
    \param _cursor database cursor
    '''
    _cursor.execute("SELECT * FROM members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_members(_cursor, row[1])

def push_into_matter_of_expense(_cursor, _name, _originator, _provider, _group, _amount, _account):
    ''' 
    \brief pushes a new entry into 'matter of expense' table
    '''
    print("    pushing 'matter_of_expense'")
    try:
        _cursor.execute("INSERT INTO matter_of_expense(name, originator, provider, group_of_expenses, amount, account) values (?,?,?,?,?,?)", (_name, _originator, _provider, _group, _amount,_account))
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])  


def pop_from_matter_of_expense(_cursor, _name, _originator, _provider, _group, _amount, _account):
    ''' 
    \brief pushes a new entry into 'matter of expense' table
    '''
    print("    deleting 'matter_of_expense'")
    try:
        _cursor.execute("DELETE FROM matter_of_expense WHERE name=? AND originator=? AND provider=? AND group_of_expenses=? AND amount=? AND account=?", (_name, _originator, _provider, _group, _amount, _account,))
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])   
    
def pop_all_from_matter_of_expense(_cursor):
    ''' 
    \brief deletes all entries into 'matter of expense' table
    '''
    _cursor.execute("SELECT * FROM matter_of_expense")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_matter_of_expense(_cursor, row[1], row[2], row[3], row[4], row[5]) 

def push_into_invoice(_cursor, _matter_of_expense, _originator, _date):
    '''
    \brief pushes a new entry into the 'invoice' table
    '''
    print("    pushing 'invoices'")
    try:
        _cursor.execute("INSERT INTO invoices(matter_of_expense, originator, date) values (?,?,?)", (_matter_of_expense, _originator, _date,))
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0]) 

def pop_from_invoice(_cursor, _matter_of_expense, _originator, _date):
    '''
    \brief deletes entry from the 'invoice' table
    '''

    print("    deleting 'matter_of_expense'")
    try:
        _cursor.execute("DELETE FROM invoices WHERE matter_of_expense=? AND originator=? AND date=?", (_matter_of_expense, _originator, _date,))
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        
def pop_all_from_invoices(_cursor):
    ''' 
    \brief deletes all entries into 'matter of expense' table
    '''
    _cursor.execute("SELECT * FROM invoices")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_invoice(_cursor, row[1], row[2], row[3]) 
    

def push_into_groups_of_expenses(_cursor, _name):
    '''
    \brief pushes a new entry into the 'group of expenses' table
    '''
    print("    pushing 'groups of expenses'")
    try:
        _cursor.execute("INSERT INTO groups_of_expenses(name) values (?)", (_name,))
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
    
def pop_from_groups_of_expenses(_cursor, _name):
    '''
    \brief pushes a new entry into the 'group of expenses' table
    '''
    print("    pushing 'groups of expenses'")
    try:
        _cursor.execute("DELETE FROM groups_of_expenses WHERE name=?", (_name,))
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])    
        
def pop_all_from_groups_of_expenses(_cursor):
    ''' 
    \brief deletes all entries into 'groups of expense' table
    '''
    _cursor.execute("SELECT * FROM groups_of_expenses")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_groups_of_expenses(_cursor, row[1]) 

def push_into_groups_of_members(_cursor, _name):
    '''
    \brief pushes into group of members
    '''
    print("    pushing 'groups of members'")
    try:
        _cursor.execute("INSERT INTO groups_of_members(name) values (?)", (_name,))
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])

def pop_from_groups_of_members(_cursor, _name):
    '''
    \brief pops from group of members
    '''
    print("    pushing 'groups of members'")
    try:
        _cursor.execute("DELETE FROM groups_of_members WHERE name=?", (_name,))
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
    
def pop_all_from_groups_of_members(_cursor):
    '''
    \brief pops from group of members
    '''
    _cursor.execute("SELECT * FROM groups_of_members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_groups_of_members(_cursor, row[1]) 

def push_into_earnings(_cursor, _name):
    '''
    \brief pushes into earnings
    '''
    print("    pushing 'earnings'")
    try:
        _cursor.execute("INSERT INTO earnings(name) values (?)", (_name,))
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])

def pop_from_earnings(_cursor, _name):
    '''
    \brief pops from earnings
    '''
    print("    pushing 'earnings'")
    try:
        _cursor.execute("DELETE FROM earnings WHERE name=?", (_name,))
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
    
def pop_all_from_earnings(_cursor):
    '''
    \brief pops from group of members
    '''
    _cursor.execute("SELECT * FROM earnings")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_earnings(_cursor, row[1]) 

def push_into_accounts(_cursor, _name):
    '''
    \brief pushes into accounts
    '''
    print("    pushing 'accounts'")
    try:
        _cursor.execute("INSERT INTO accounts(name) values (?)", (_name,))
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])

def pop_from_accounts(_cursor, _name):
    '''
    \brief pops from accounts
    '''
    print("    pushing 'accounts'")
    try:
        _cursor.execute("DELETE FROM accounts WHERE name=?", (_name,))
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
    
def pop_all_from_accounts(_cursor):
    '''
    \brief pops from group of members
    '''
    _cursor.execute("SELECT * FROM earnings")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_earnings(_cursor, row[1]) 

def show_all_members(_cursor):
    for row in _cursor.execute("select * from members"):
        print(row)

def show_all_matter_of_expense(_cursor):
    for row in _cursor.execute("select * from matter_of_expenses"):
        print(row)
        
def show_all_invoices(_cursor):
    for row in _cursor.execute("select * from invoices"):
        print(row)

def show_all_groups_of_members(_cursor):
    for row in _cursor.execute("select * from groups_of_members"):
        print(row)

def show_all_groups_of_expenses(_cursor):
    for row in _cursor.execute("select * from groups_of_expenses"):
        print(row)

def show_all_earnings(_cursor):
    for row in _cursor.execute("select * from earnings"):
        print(row)

def show_all_accounts(_cursor):
    for row in _cursor.execute("select * from accounts"):
        print(row)
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
