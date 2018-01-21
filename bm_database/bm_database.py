#!/usr/bin/python3 
# coding=latin-1
import sys
import sqlite3
import os

conn = 0

def main():
    ''' 
    @brief main routine
    \return void
    '''
    c= connect()
    setup_db(c)
    disconnect(c)

def connect():
    ''' 
    @brief connect to the database
    '''
    global conn
    conn = sqlite3.connect("budget_management.db")
    c = conn.cursor()
    return c

def disconnect(_cursor):
    ''' 
    @brief disconnect from the database
    '''
    _cursor.close()

def setup_db(_cursor):
    ''' 
    @brief setup the database
    
    @param _cursor    database cursor
    '''
    print("setting up the database as well as the tables")
   
    for i in range(0,7):
        try:
            if i == 0:
                _cursor.execute("CREATE TABLE members (id integer primary key, name text unique, group_of_members integer)")
            elif i == 1:
                _cursor.execute("CREATE TABLE matter_of_expense (id integer primary key, name text, originator integer, provider name, group_of_expenses integer, amount float, frequency text, account integer)")
            elif i == 2:
                _cursor.execute("CREATE TABLE invoices (id integer primary key, matter_of_expense integer, originator integer, date text)")
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
    @brief destroy the database again
    
    @param _cursor    database cursor
    '''
    
    print("destroying the database which includes the tables")
    
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
    @brief pushes a new entry into 'members' table
    
    @param _cursor   database cursor
    @param _name     member's name
    @param _group    member's group ID
    '''
    print("    pushing member")
    try:
        global conn
        
        _cursor.execute("INSERT INTO members(name, group_of_members) values (?,?)", (_name, _group,))
        
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1                 

def pop_from_members(_cursor, _name):
    ''' 
    @brief pops a new entry into 'members' table
    
    @param _cursor   database cursor
    @param _name     member's name
    @param _group    member's group ID
    '''
    print("    pop from member")
    try:
        global conn
        _cursor.execute("DELETE FROM members WHERE name=?", (_name,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1
    


def pop_all_from_members(_cursor):
    '''
    @brief pop all entries from the 'member' table
    
    @param _cursor database cursor
    '''
    global conn
    _cursor.execute("SELECT * FROM members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_members(_cursor, row[1])

    conn.commit()
    
    
def show_all_members(_cursor):
    '''
    @brief shows all members
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from members"):
        print(row)
        
def get_entries_members(_cursor):
    '''
    @brief returns all entries from members
    '''
    entries=[]    
    _cursor.execute("select * from members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append(row[1])
        
    return entries
        

def select_from_members_where_name_match(_cursor, _name):
    '''
    @brief selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM members WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def push_into_matter_of_expense(_cursor, _name, _originator, _provider, _group, _amount, _frequency, _account):
    ''' 
    @brief pushes a new entry into 'matter of expense' table
    '''
    print("    pushing 'matter_of_expense'")
    try:
        global conn
        _cursor.execute("INSERT INTO matter_of_expense(name, originator, provider, group_of_expenses, amount, frequency, account) values (?,?,?,?,?,?,?)", (_name, _originator, _provider, _group, _amount, _frequency, _account))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1  

def pop_from_matter_of_expense(_cursor, _name, _originator, _provider, _group, _amount, _frequency, _account):
    ''' 
    @brief pushes a new entry into 'matter of expense' table
    '''
    print("    deleting 'matter_of_expense'")
    try:
        global conn
        _cursor.execute("DELETE FROM matter_of_expense WHERE name=? AND originator=? AND provider=? AND group_of_expenses=? AND amount=? AND frequency=?AND account=?", (_name, _originator, _provider, _group, _amount, _frequency, _account,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1   
    
def pop_all_from_matter_of_expense(_cursor):
    ''' 
    @brief deletes all entries into 'matter of expense' table
    '''
    global conn
    _cursor.execute("SELECT * FROM matter_of_expense")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_matter_of_expense(_cursor, row[1], row[2], row[3], row[4], row[5], row[6], row[7]) 
    conn.commit()

def select_from_matter_of_expense_where_name_match(_cursor, _name):
    '''
    @brief selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM matter_of_expense WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def show_all_matter_of_expense(_cursor):
    '''
    @brief shows all matter of expenses
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from matter_of_expense"):
        print(row)
        
def get_entries_matter_of_expense(_cursor):
    '''
    @brief returns all entries from members
    @return string
    '''    
    entries = []
    
    for row in _cursor.execute("select * from matter_of_expense"):
        entries.append(row)
        
    return entries
        
def show_all_groups_of_expenses(_cursor):
    '''
    @brief shows all group of expenses
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from groups_of_expenses"):
        print(row)

def push_into_invoice(_cursor, _matter_of_expense, _originator, _date):
    '''
    @brief pushes a new entry into the 'invoice' table
    '''
    print("    pushing 'invoices'")
    try:
        global conn
        _cursor.execute("INSERT INTO invoices(matter_of_expense, originator, date) values (?,?,?)", (_matter_of_expense, _originator, _date,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1 

def pop_from_invoice(_cursor, _matter_of_expense, _originator, _date):
    '''
    @brief deletes entry from the 'invoice' table
    '''

    print("    deleting 'invoices'")
    try:
        global conn
        _cursor.execute("DELETE FROM invoices WHERE matter_of_expense=? AND originator=? AND date=?", (_matter_of_expense, _originator, _date,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1
        
def pop_all_from_invoices(_cursor):
    ''' 
    @brief deletes all entries into 'matter of expense' table
    '''
    global conn
    _cursor.execute("SELECT * FROM invoices")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_invoice(_cursor, row[1], row[2], row[3])
    
    conn.commit() 

def show_all_invoices(_cursor):
    '''
    @brief shows all invoices
    
    @param cursor    database cursor            refresh()
    '''
    for row in _cursor.execute("select * from invoices"):
        print(row)
        
def get_entries_invoices(_cursor):
    '''
    @brief returns all entries from invoices
    @return string
    '''    
    
    # we need a variable in order to return the etnries
    entries = []
    
    for row in _cursor.execute("select * from invoices"):
        entries.append(row)
    return entries
        
def select_from_invoices_where_matter_of_expense_match(_cursor, _matter_of_expense):
    '''
    @brief selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM invoices WHERE matter_of_expense=?", (_matter_of_expense,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def push_into_groups_of_expenses(_cursor, _name):
    '''
    @brief pushes a new entry into the 'group of expenses' table
    '''
    print("    pushing 'groups of expenses'")
    try:
        global conn
        _cursor.execute("INSERT INTO groups_of_expenses(name) values (?)", (_name,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1
    
def pop_from_groups_of_expenses(_cursor, _name):
    '''
    @brief pushes a new entry into the 'group of expenses' table
    '''
    print("    pushing 'groups of expenses'")
    try:
        global conn
        _cursor.execute("DELETE FROM groups_of_expenses WHERE name=?", (_name,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1    
        
def pop_all_from_groups_of_expenses(_cursor):
    ''' 
    @brief deletes all entries into 'groups of expense' table
    '''
    global conn
    _cursor.execute("SELECT * FROM groups_of_expenses")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1])
        pop_from_groups_of_expenses(_cursor, row[1])
        
    conn.commit() 
    
def get_entries_groups_of_expenses(_cursor):
    '''
    @brief returns all entries from accounts
    '''
    entries=[]    
    _cursor.execute("select * from groups_of_expenses")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append(row[1])
        
    return entries

def select_from_groups_of_expense_where_name_match(_cursor, _name):
    '''
    @brief selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM groups_of_expenses WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def push_into_groups_of_members(_cursor, _name):
    '''
    @brief pushes into group of members
    '''
    print("    pushing 'groups of members'")
    try:
        global conn
        _cursor.execute("INSERT INTO groups_of_members(name) values (?)", (_name,))
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])

def pop_from_groups_of_members(_cursor, _name):
    '''
    @brief pops from group of members
    '''
    print("    pushing 'groups of members'")
    try:
        global conn
        _cursor.execute("DELETE FROM groups_of_members WHERE name=?", (_name,))
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
    
def pop_all_from_groups_of_members(_cursor):
    '''
    @brief pops from group of members
    '''
    global conn
    _cursor.execute("SELECT * FROM groups_of_members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_groups_of_members(_cursor, row[1])
    conn.commit()
    
def get_entries_groups_of_members(_cursor):
    '''
    @brief returns all entries from groups of members
    '''
    entries=[]    
    _cursor.execute("select * from groups_of_members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append(row[1])
        
    return entries
        
def select_from_groups_of_members_where_name_match(_cursor, _name):
    '''
    @brief selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM groups_of_members WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def show_all_groups_of_members(_cursor):
    '''
    @brief shows all group of members
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from groups_of_members"):
        print(row)

def push_into_earnings(_cursor, _name, _account, _amount):
    '''
    @brief pushes into earnings
    '''
    print("    pushing 'earnings'")
    try:
        global conn
        _cursor.execute("INSERT INTO earnings(name, account, amount) values (?, ?, ?)", (_name, _account, _amount))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1

def pop_from_earnings(_cursor, _name):
    '''
    @brief pops from earnings
    '''
    print("    pushing 'earnings'")
    try:
        global conn
        _cursor.execute("DELETE FROM earnings WHERE name=?", (_name,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1
    
def pop_all_from_earnings(_cursor):
    '''
    @brief pops from group of members
    '''
    global conn
    _cursor.execute("SELECT * FROM earnings")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_earnings(_cursor, row[1])
    conn.commit() 

def get_entries_earnings(_cursor):
    '''
    @brief returns all entries from earnings
    '''
    entries=[]    
    _cursor.execute("select * from earnings")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append(row[1])
        
    return entries

def select_from_earnings_where_name_match(_cursor, _name):
    '''
    @brief selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM earnings WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def show_all_earnings(_cursor):
    '''
    @brief shows all earnings
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from earnings"):
        print(row)

def push_into_accounts(_cursor, _name):
    '''
    @brief pushes into accounts
    '''
    print("    pushing 'accounts'")
    try:
        global conn
        _cursor.execute("INSERT INTO accounts(name) values (?)", (_name,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1

def pop_from_accounts(_cursor, _name):
    '''
    @brief pops from accounts
    '''
    print("    pushing 'accounts'")
    try:
        global conn
        _cursor.execute("DELETE FROM accounts WHERE name=?", (_name,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1
    
def pop_all_from_accounts(_cursor):
    '''
    @brief pops from group of members
    '''
    global conn
    _cursor.execute("SELECT * FROM earnings")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_earnings(_cursor, row[1])
    conn.commit() 

def get_entries_accounts(_cursor):
    '''
    @brief returns all entries from accounts
    '''
    entries=[]    
    _cursor.execute("select * from accounts")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append(row[1])
        
    return entries

def select_from_accounts_where_name_match(_cursor, _name):
    '''
    @brief selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM accounts WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def show_all_accounts(_cursor):
    '''
    @brief shows all accounts
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from accounts"):
        print(row)
            
if __name__ == "__main__":
    # execute only if run as a script
    main()
