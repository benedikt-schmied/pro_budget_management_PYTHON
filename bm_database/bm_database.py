#!/usr/bin/python3 
# coding=latin-1
import sys
import sqlite3
import os

def main():
    c=setup_db()
    
def setup_db():
    print("setting up the database as well as the tables")
    conn = sqlite3.connect("budget_management.db")
    c=conn.cursor()
    
    for i in range(0,5):
        try:
            if i == 0:
                c.execute("CREATE TABLE members (id integer primary key, name text, group_of_members integer)")
            elif i == 1:
                c.execute("CREATE TABLE matter_of_expense (id integer primary key, name text, originator integer, provider name, group_of_expenses integer, amount float)")
            elif i == 2:
                c.execute("CREATE TABLE invoices (id integer primary key, matter_of_expense integer, integer originator, date text)")
            elif i == 3:
                c.execute("CREATE TABLE groups_of_expenses (id integer primary key, name text)")
            elif i == 4:
                c.execute("CREATE TABLE groups_of_members (id integer primary key, name text)")    
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
    return c

def push_into_members(_cursor, _name, _group):
    ''' \brief pushes a new entry into 'members' table
    '''
    print("    pushing member")
    try:
        _cursor.execute("INSERT INTO members(name, group_of_members) values (?,?)", (_name, _group,))
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])                 

def push_into_matter_of_expense(_cursor, _name, _originator, _provider, _group, _amount):
    ''' \brief pushes a new entry into 'members' table
    '''
    print("    pushing 'matter_of_expense'")
    try:
        _cursor.execute("INSERT INTO matter_of_expense(name, originator, provider, group_of_expenses, amount) values (?,?,?,?,?)", (_name, _originator, _provider, _group, _amount,))
    except sqlite3.Error as e:
        print("An error occurred:", e.args[0])  
        
def push_into_invoice(_cursor, _matter_of_expense, _originator, _date):
    print("    pushing 'invoices'")
    _cursor.execute("INSERT INTO invoices(matter_of_expense, originator, _date) values (?,?,?)", (_matter_of_expense, _originator, _date,))
    print("    dublicate album encountered")

def push_into_groups_of_expenses(_cursor, _name):
    print("    pushing 'groups of expenses'")
    _cursor.execute("INSERT INTO groups_of_expenses(_name) values (?)", (_name,))

def push_into_groups_of_members(_cursor, _name):
    print("    pushing 'groups of members'")
    _cursor.execute("INSERT INTO groups_of_members(_name) values (?)", (_name,))

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

def get_artist(cursor, name):
    print("    searching for artist")
    try:
        cursor.execute("select artists.id from artists where artists.name=? ", (name,))
        r=cursor.fetchone()
        type(r)
        r[0]
        return r[0]
    except:
        print("    did not find anything")
        return

def get_album(cursor, name, artist):
    print("    searching for album")

    cursor.execute("select album.id from album where album.name=? and album.artist=? ", (name,artist,))
    r=cursor.fetchone()
    type(r)
    r[0]
    return r[0]

def setup_eyed3():
    print("    setting up the eyed3 plugin")
    
if __name__ == "__main__":
    # execute only if run as a script
    main()
