#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')

import sqlite3
from collections import namedtuple


''' database definitions
first, there comes a nametuple in order to ease data retrivals
second, there is a dictionary which holds the data types for each column
'''

# table of members
t_bm_table_members = namedtuple('t_bm_table_members', ['id', 'name', 'group_of_members'])

s_bm_table_members = {'id': 'integer primary key', 'name': 'text unique', 'group_of_members': 'integer'}

# matter of expenses 
t_bm_table_matter_of_expenses = namedtuple('t_bm_table_matter_of_expenses', [ \
    'id', 'name', 'originator', 'originator_class', 'provider', 'provider_class', \
    'groups_of_expenses', 'amount', 'frequency', 'account'\
    ])

s_bm_table_matter_of_expenses = {'id': 'integer primary key', 'name': 'text', 'originator_class': 'integer', 'originator': 'integer', \
    'provider_class': 'integer', 'provider': 'integer', 'group_of_expenses': 'integer', 'amount': 'float', \
    'frequency': 'integer', 'account': 'integer'}

# invoices
t_bm_table_invoice = namedtuple('t_bm_table_invoice', [ \
    'id', 'matter_of_expense', 'originator_class', 'originator', 'date' \
   ]) 

s_bm_table_invoice = {'id': 'primary key', 'matter_of_expense': 'integer', 'originator_class': 'integer', \
    'originator': 'integer', 'data': 'text'}

# groups of expenses
t_bm_table_groups_expenses = namedtuple('t_bm_table_groups_expenses', [\
    'id', 'name' \
    ]) 

s_bm_table_groups_of_expenses = {'id': 'integer primary key', 'name': 'text unique'}

# groups of members
t_bm_table_groups_of_members = namedtuple('t_bm_table_groups_of_members', [\
    'id', 'name' \
    ])

s_bm_table_groups_of_members = {'id': 'integer primary key', 'name': 'text unique'}

# earnings
t_bm_table_earnings = namedtuple('t_bm_table_earnings', [ \
    'id', 'name', 'account', 'amount' \
    ])

s_bm_table_earnings = {'id': 'integer primary key', 'name': 'text unique', 'account': 'integer', 'amount': 'integer'}

# accounts
t_bm_table_accounts = namedtuple('t_bm_table_accounts', [\
    'id', 'name' \
    ])

s_bm_table_earnings = {'id': 'integer primary key', 'name': 'text unique'}

# table of classes
t_bm_table_class = namedtuple('t_bm_table_class', [\
    'id', 'name'\
    ])

s_bm_table_class = {'id': 'integer primary key', 'name': 'text unigue'}


def retrieve_definition_member(_idx):
    ''' returns the defining string for this table
    @param _idx: index
    '''
    if _idx == 0:
        return 'integer primary key'
    elif _idx == 1:
        return 'text unique'
    elif _idx == 2:
        return 'integer'
    else:
        return 'error' # returning this string will cause the SQL statement to fail
    
def retrieve_definition_matter_of_expense(_idx):
    ''' returns the defining string for this table
    '''
    if _idx == 0:
        return 'integer primary key'
    if _idx == 1:
        return 'text'
    if (_idx == 2) or (_idx == 3) or (_idx == 4) or (_idx == 5) or (_idx == 6) or (_idx == 8) or (_idx == 9):
        return 'integer'
    if (_idx == 7):
        return 'float'

conn = 0

def main():
    '''    main routine
    \return void
    '''
    c= connect()
    setup_db(c)
    disconnect(c)

def connect():
    '''    connect to the database
    '''
    global conn
    conn = sqlite3.connect("budget_management.db")
    c = conn.cursor()
    return c

def disconnect(_cursor):
    '''    disconnect from the database
    '''
    _cursor.close()

class c_tables():
    
    def __init__(self, _name, _fun, _fields):
        self.name = _name
        self.fun = _fun
        self.fields = _fields

    def get_name(self):
        return self.name
    
    def get_fun(self):
        return self.fun

    def get_fields(self):
        return self.fields

def setup_db(_cursor):
    '''    setup the database
    
    @param _cursor    database cursor
    '''
    print("setting up the database as well as the tables")
   
    
   
   
    for i in range(0,8):
        
        cmdstr = "CREATE TABLE "
        
        try:
            if i == 0:
                
                # start the specific entry within the command string
                cmdstr = cmdstr + "members ("
                
                # loop over all fields
                for cnt in range(0, len(t_bm_table_members._fields)):
                    cmdstr = cmdstr + "{} {}".format(t_bm_table_members._fields[cnt], retrieve_definition_member(cnt))
                    
                    if cnt < (len(t_bm_table_members._fields) - 1):
                        cmdstr = cmdstr + ", "
                
                cmdstr = cmdstr + ")"
                _cursor.execute(cmdstr)
            elif i == 1:
                
                # start the specific entry within the command string
                cmdstr = cmdstr + "matter_of_expense ("
                
                # loop over all fields
                for cnt in range(0, len(t_bm_table_matter_of_expenses._fields)):
                    cmdstr = cmdstr + "{} {}".format(t_bm_table_matter_of_expenses._fields[cnt], retrieve_definition_matter_of_expense(cnt))
                
                    if cnt < (len(t_bm_table_members._fields) - 1):
                        cmdstr = cmdstr + ", "
                
                cmdstr = cmdstr + ")"
                _cursor.execute(cmdstr)
            elif i == 2:
                _cursor.execute("CREATE TABLE invoices (id integer primary key, matter_of_expense integer, originator_class integer, originator integer, date text)")
            elif i == 3:
                _cursor.execute("CREATE TABLE groups_of_expenses (id integer primary key, name text unique)")
            elif i == 4:
                _cursor.execute("CREATE TABLE groups_of_members (id integer primary key, name text unique)")
            elif i == 5:
                _cursor.execute("CREATE TABLE earnings (id integer primary key, name text unique, account integer, amount integer)")    
            elif i == 6:
                _cursor.execute("CREATE TABLE accounts (id integer primary key, name text unique)")
            elif i == 7:
                _cursor.execute("CREATE TABLE class (id integer primary key, name text unigue)")
                        
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
    
    global conn 
    conn.commit()
    
    return _cursor

def destroy_db(_cursor):
    '''   destroy the database again
    
    @param _cursor    database cursor
    '''
    
    print("destroying the database which includes the tables")
    
    for i in [7,6,5,4,3,2,1,0]:
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
            elif i == 7:
                _cursor.execute("DROP Table classes")
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
    global conn
    conn.commit()
    return _cursor
    
def manual_db_command(_cursor, _text):
    _cursor.execute(_text)
    global conn
    conn.commit
    

def push_into_members(_cursor, _name, _group):
    '''    pushes a new entry into 'members' table
    
    @param _cursor   database cursor
    @param _name     member's name
    @param _group    member's group ID
    '''
#     print("    pushing member")
#     try:
    global conn
     
    _cursor.execute("INSERT INTO members(name, group_of_members) values (?,?)", (_name, _group,))
     
    conn.commit()
    return 0
#     except sqlite3.Error as e:
#         print("An error occurred:", e.args[0])
#         return -1                 

def pop_from_members(_cursor, _name):
    '''    pops a new entry into 'members' table
    
    @param _cursor   database cursor
    @param _name     member's name
    '''
    print("    pop from member '{}'".format(_name))
    try:
        global conn
        _cursor.execute("DELETE FROM members WHERE name=?", (_name,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1
    
def pop_from_members_where_id(_cursor, _id):
    '''    pops a new entry into 'members' table
    
    @param _cursor   database cursor
    @param _name     member's name
    '''
    try:
        global conn
        _cursor.execute("DELETE FROM members WHERE id=?", (_id,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1

def pop_all_from_members(_cursor):
    '''   pop all entries from the 'member' table
    
    @param _cursor database cursor
    '''
    global conn
    _cursor.execute("SELECT * FROM members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1])
        pop_from_members(_cursor, row[1])

    conn.commit()
    
    
def show_all_members(_cursor):
    '''   shows all members
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from members"):
        print(row)
        
def get_entries_members(_cursor):
    '''   returns all entries from members
    '''
    entries=[]    
    _cursor.execute("select * from members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append([row[0], row[1], row[2]])
        
    return entries
        

def select_from_members_where_name_match(_cursor, _name):
    '''   selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM members WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def update_in_members_where_id_match(_cursor, _id, _entries):
    '''    selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM members WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def push_into_matter_of_expense(_cursor, _name, _originator_class, _originator, _provider_class, _provider, _group, _amount, _frequency, _account):
    '''    pushes a new entry into 'matter of expense' table
    '''
    print("    pushing 'matter_of_expense'")
    try:
        global conn
        _cursor.execute("INSERT INTO matter_of_expense(name, originator_class, originator, provider_class, provider, group_of_expenses, amount, frequency, account) values (?,?,?,?,?,?,?,?,?)", (_name, _originator_class, _originator, _provider_class, _provider, _group, _amount, _frequency, _account))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1  

def pop_from_matter_of_expense(_cursor, _name, _originator_class, _originator, _provider_class, _provider, _group, _amount, _frequency, _account):
    '''   pushes a new entry into 'matter of expense' table
    '''
    print("    deleting 'matter_of_expense'")
    try:
        global conn
        _cursor.execute("DELETE FROM matter_of_expense WHERE name=? AND originator_class=? AND originator=? AND provider_class=? AND provider=? AND group_of_expenses=? AND amount=? AND frequency=?AND account=?", (_name, _originator_class, _originator, _provider_class, _provider, _group, _amount, _frequency, _account,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1
    
def pop_from_matter_of_expense_where_id(_cursor, _id):
    '''    pushes a new entry into 'matter of expense' table
    '''
    print("    deleting 'matter_of_expense'")
    try:
        global conn
        _cursor.execute("DELETE FROM matter_of_expense WHERE id=? ", (_id,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1      
    
def pop_all_from_matter_of_expense(_cursor):
    '''    deletes all entries into 'matter of expense' table
    '''
    global conn
    _cursor.execute("SELECT * FROM matter_of_expense")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_matter_of_expense(_cursor, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) 
    conn.commit()

def select_from_matter_of_expense_where_name_match(_cursor, _name):
    '''   selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM matter_of_expense WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def show_all_matter_of_expense(_cursor):
    '''   shows all matter of expenses
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from matter_of_expense"):
        print(row)
        
def get_entries_matter_of_expense(_cursor):
    '''   returns all entries from members
    @return string
    '''    
    entries = []
    
    for row in _cursor.execute("select * from matter_of_expense"):
        entries.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])
        
    return entries
        
def show_all_groups_of_expenses(_cursor):
    '''   shows all group of expenses
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from groups_of_expenses"):
        print(row)

def push_into_invoice(_cursor, _matter_of_expense, _originator_class, _originator, _date):
    '''   pushes a new entry into the 'invoice' table
    '''
    print("    pushing 'invoices'")
    try:
        global conn
        _cursor.execute("INSERT INTO invoices(matter_of_expense, originator_class, originator, date) values (?,?,?,?)", (_matter_of_expense, _originator_class, _originator, _date,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])
        return -1 

def pop_from_invoice(_cursor, _matter_of_expense, _originator_class, _originator, _date):
    '''   deletes entry from the 'invoice' table
    '''

    print("    deleting 'invoices'")
    try:
        global conn
        _cursor.execute("DELETE FROM invoices WHERE matter_of_expense=? AND originator_class=? AND originator=? AND date=?", (_matter_of_expense, _originator_class, _originator, _date,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1

def pop_from_invoice_where_id(_cursor, _id):
    '''   deletes entry from the 'invoice' table
    '''

    print("    deleting 'invoices'")
    try:
        global conn
        _cursor.execute("DELETE FROM invoices WHERE id=?", (_id,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1

def pop_all_from_invoices(_cursor):
    '''    deletes all entries into 'matter of expense' table
    '''
    global conn
    _cursor.execute("SELECT * FROM invoices")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_invoice(_cursor, row[1], row[2], row[3], row[4])
    
    conn.commit() 

def show_all_invoices(_cursor):
    '''   shows all invoices
    
    @param cursor    database cursor            refresh()
    '''
    for row in _cursor.execute("select * from invoices"):
        print(row)
        
def get_entries_invoices(_cursor):
    '''   returns all entries from invoices
    @return string
    '''    
    
    # we need a variable in order to return the etnries
    entries = []
    
    for row in _cursor.execute("select * from invoices"):
        entries.append(row)
    return entries
        
def select_from_invoices_where_matter_of_expense_match(_cursor, _matter_of_expense):
    '''   selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM invoices WHERE matter_of_expense=?", (_matter_of_expense,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def push_into_groups_of_expenses(_cursor, _name):
    '''   pushes a new entry into the 'group of expenses' table
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
    '''   pushes a new entry into the 'group of expenses' table
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
    
def pop_from_groups_of_expenses_where_id(_cursor, _id):
    '''   pushes a new entry into the 'group of expenses' table
    '''
    print("    pushing 'groups of expenses'")
    try:
        global conn
        _cursor.execute("DELETE FROM groups_of_expenses WHERE id=?", (_id,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1   
        
def pop_all_from_groups_of_expenses(_cursor):
    '''    deletes all entries into 'groups of expense' table
    '''
    global conn
    _cursor.execute("SELECT * FROM groups_of_expenses")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1])
        pop_from_groups_of_expenses(_cursor, row[1])
        
    conn.commit() 
    
def get_entries_groups_of_expenses(_cursor):
    '''   returns all entries from accounts
    '''
    entries=[]    
    _cursor.execute("select * from groups_of_expenses")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append([row[0], row[1]])
        
    return entries

def select_from_groups_of_expense_where_name_match(_cursor, _name):
    '''   selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM groups_of_expenses WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def push_into_groups_of_members(_cursor, _name):
    '''   pushes into group of members
    '''
    print("    pushing 'groups of members'")
    try:
        global conn
        _cursor.execute("INSERT INTO groups_of_members(name) values (?)", (_name,))
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])

def pop_from_groups_of_members(_cursor, _name):
    '''   pops from group of members
    '''
    print("    pushing 'groups of members'")
    try:
        global conn
        _cursor.execute("DELETE FROM groups_of_members WHERE name=?", (_name,))
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])


def pop_from_groups_of_members_where_id(_cursor, _id):
    '''   pops from group of members
    '''
    print("    pushing 'groups of members'")
    try:
        global conn
        _cursor.execute("DELETE FROM groups_of_members WHERE id=?", (_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
    
def pop_all_from_groups_of_members(_cursor):
    '''   pops from group of members
    '''
    global conn
    _cursor.execute("SELECT * FROM groups_of_members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_groups_of_members(_cursor, row[1])
        
    conn.commit()
    
def get_entries_groups_of_members(_cursor):
    '''   returns all entries from groups of members
    '''
    entries=[]    
    _cursor.execute("select * from groups_of_members")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append([row[0], row[1]])
        
    return entries
        
def select_from_groups_of_members_where_name_match(_cursor, _name):
    '''   selects a specific entry where the name matches
    
    @param _cursor database cursor
d    '''   
    try:
        _cursor.execute("SELECT id FROM groups_of_members WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def show_all_groups_of_members(_cursor):
    '''   shows all group of members
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from groups_of_members"):
        print(row)

def push_into_earnings(_cursor, _name, _account, _amount):
    '''   pushes into earnings
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
    '''   pops from earnings
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
    
def pop_from_earnings_where_id(_cursor, _id):
    '''   pops from earnings
    '''
    print("    pushing 'earnings'")
    try:
        global conn
        _cursor.execute("DELETE FROM earnings WHERE id=?", (_id,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1
    
def pop_all_from_earnings(_cursor):
    '''   pops from group of members
    '''
    global conn
    _cursor.execute("SELECT * FROM earnings")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_earnings(_cursor, row[1])
    conn.commit() 

def get_entries_earnings(_cursor):
    '''   returns all entries from earnings
    '''
    entries=[]    
    _cursor.execute("select * from earnings")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append([row[0], row[1], row[2], row[3]])
        
    return entries

def select_from_earnings_where_name_match(_cursor, _name):
    '''   selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM earnings WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def show_all_earnings(_cursor):
    '''   shows all earnings
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from earnings"):
        print(row)

def push_into_accounts(_cursor, _name):
    '''   pushes into accounts
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
    '''   pops from accounts
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
 
def pop_from_accounts_where_id(_cursor, _id):
    '''   pops from accounts
    '''
    print("    pushing 'accounts'")
    try:
        global conn
        _cursor.execute("DELETE FROM accounts WHERE id=?", (_id,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1
   
def pop_all_from_accounts(_cursor):
    '''   pops from group of members
    '''
    global conn
    _cursor.execute("SELECT * FROM earnings")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_earnings(_cursor, row[1])
    conn.commit() 

def get_entries_accounts(_cursor):
    '''   returns all entries from accounts
    '''
    entries=[]    
    _cursor.execute("select * from accounts")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append([row[0], row[1]])
        
    return entries

def select_from_accounts_where_name_match(_cursor, _name):
    '''   selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM accounts WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def show_all_accounts(_cursor):
    '''   shows all accounts
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from accounts"):
        print(row)
        
def push_into_class(_cursor, _name):
    '''   pushes into class
    '''
    print("    pushing 'class'")
    try:
        global conn
        _cursor.execute("INSERT INTO class(name) values (?)", (_name,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1

def pop_from_class(_cursor, _name):
    '''   pops from class
    '''
    print("    pushing 'class'")
    try:
        global conn
        _cursor.execute("DELETE FROM class WHERE name=?", (_name,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1
 
def pop_from_class_where_id(_cursor, _id):
    '''   pops from class
    '''
    print("    pushing 'class'")
    try:
        global conn
        _cursor.execute("DELETE FROM class WHERE id=?", (_id,))
        conn.commit()
        return 0
    except sqlite3.Error as e:
        print("An error occurred: ", e.args[0])
        return -1
   
def pop_all_from_class(_cursor):
    '''   pops from group of members
    '''
    global conn
    _cursor.execute("SELECT * FROM earnings")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        print("deleting ", row[1], row[2])
        pop_from_earnings(_cursor, row[1])
    conn.commit() 

def get_entries_class(_cursor):
    '''   returns all entries from class
    '''
    entries=[]    
    _cursor.execute("select * from class")
    list_of_members = _cursor.fetchall()
    for row in list_of_members:
        entries.append([row[0], row[1]])
        
    return entries

def select_from_class_where_name_match(_cursor, _name):
    '''   selects a specific entry where the name matches
    
    @param _cursor database cursor
    '''   
    try:
        _cursor.execute("SELECT id FROM class WHERE name=?", (_name,))
        return _cursor.fetchone()[0]
    except sqlite3.Error as e:
        print("An error occrred: ", e.args[0])
        return -1

def show_all_class(_cursor):
    '''   shows all class
    
    @param cursor    database cursor
    '''
    for row in _cursor.execute("select * from class"):
        print(row)
            
if __name__ == "__main__":
    # execute only if run as a script
    main()
