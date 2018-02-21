#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
from bm_globals import *
import mod_logging_mkI_PYTHON
import sqlite3
from collections import namedtuple

g_program_suffix = "bm_database"

''' database definitions
first, there comes a namedtuple in order to ease data retrivals
second, there is a dictionary which holds the data types for each column
'''

# table of members

# long definition which contains the ID as well
t_bm_members_l = namedtuple('t_bm_members_l', ['id', 'name', 'group_of_members'])

# short definition which does not contain the ID
t_bm_members_s = namedtuple('t_bm_members_s', ['name', 'group_of_members'])

s_bm_table_members = {'id': 'integer primary key', 'name': 'text unique', 'group_of_members': 'integer'}

# matter of expenses 
t_bm_matter_of_expenses_l = namedtuple('t_bm_matter_of_expenses_l', [ \
    'id', 'name', 'originator', 'originator_class', 'provider', 'provider_class', \
    'groups_of_expenses', 'amount', 'frequency', 'account'\
    ])

t_bm_matter_of_expenses_s = namedtuple('t_bm_matter_of_expenses_s', [ \
    'name', 'originator', 'originator_class', 'provider', 'provider_class', \
    'groups_of_expenses', 'amount', 'frequency', 'account'\
    ])

s_bm_table_matter_of_expenses = {'id': 'integer primary key', 'name': 'text', 'originator_class': 'integer', 'originator': 'integer', \
    'provider_class': 'integer', 'provider': 'integer', 'group_of_expenses': 'integer', 'amount': 'float', \
    'frequency': 'integer', 'account': 'integer'}

# invoices
t_bm_table_invoice_l = namedtuple('t_bm_table_invoice_l', [ \
    'id', 'matter_of_expense', 'originator_class', 'originator', 'date' \
   ]) 

t_bm_table_invoice_s = namedtuple('t_bm_table_invoice_s', [ \
    'matter_of_expense', 'originator_class', 'originator', 'date' \
   ]) 

s_bm_table_invoice = {'id': 'primary key', 'matter_of_expense': 'integer', 'originator_class': 'integer', \
    'originator': 'integer', 'data': 'text'}

# groups of expenses
t_bm_table_groups_of_expenses_l = namedtuple('t_bm_table_groups_of_expenses_l', [\
    'id', 'name' \
    ]) 

t_bm_table_groups_of_expenses_s = namedtuple('t_bm_table_groups_of_expenses_s', [\
    'name' \
    ]) 

s_bm_table_groups_of_expenses = {'id': 'integer primary key', 'name': 'text unique'}

# groups of members
t_bm_table_groups_of_members_l = namedtuple('t_bm_table_groups_of_members_l', [\
    'id', 'name' \
    ])

t_bm_table_groups_of_members_s = namedtuple('t_bm_table_groups_of_members_s', [\
    'name' \
    ])

s_bm_table_groups_of_members = {'id': 'integer primary key', 'name': 'text unique'}

# earnings
t_bm_table_earnings_l = namedtuple('t_bm_table_earnings_l', [ \
    'id', 'name', 'account', 'amount' \
    ])

t_bm_table_earnings_l = namedtuple('t_bm_table_earnings_s', [ \
    'name', 'account', 'amount' \
    ])

s_bm_table_earnings = {'id': 'integer primary key', 'name': 'text unique', 'account': 'integer', 'amount': 'integer'}

# accounts
t_bm_table_accounts_l = namedtuple('t_bm_table_accounts_l', [\
    'id', 'name' \
    ])

t_bm_table_accounts_s = namedtuple('t_bm_table_accounts_s', [\
    'name' \
    ])

s_bm_table_accounts = {'id': 'integer primary key', 'name': 'text unique'}

# table of classes
t_bm_table_class_l = namedtuple('t_bm_table_class_l', [\
    'id', 'name'\
    ])

t_bm_table_class_s = namedtuple('t_bm_table_class_s', [\
    'id', 'name'\
    ])

s_bm_table_class = {'id': 'integer primary key', 'name': 'text unigue'}

class c_bm_database():
    ''' database class
    '''
    def __init__(self):
        self.conn = None
        self.cursor = None
        return
    
    def connect(self):
        '''    connect to the database
        '''
        self.conn = sqlite3.connect("test.db")
        self.cursor = self.conn.cursor()
        return (self.conn, self.cursor)
    
    def disconnect(self):
        ''' disconnect from the database
        '''
        self.cursor.close()
        return 
        
    def manual_db_command(self, _text):
        self.cursor.execute(_text)
        self.conn.commit

class c_bm_tables(mod_logging_mkI_PYTHON.c_sublogging):
    ''' father class for tables
    
    class members 
    fun  function
    fields fields
    name name
    '''
    
    def __init__(self, _name, _fun, _conn, _cursor, _ttuple, _tset):
        ''' constructors which builds up a table
        
        @param _name: name
        @param _fun: function
        @param _fields: fields 
        ''' 
        
        # call the sublogger's constructor
        mod_logging_mkI_PYTHON.c_sublogging.__init__(self, g_program_name + ".{}.{}".format(g_program_suffix, _name))
        
        # assign the specific name of the table
        self.name = _name
        
        # what does function mean?
        self.fun = _fun
        
        # assign the tuples as well as the set
        self.ttuples = _ttuple
        self.tsets = _tset

        # assign the cursor and the database connection
        self.conn = _conn
        self.cursor = _cursor
        
    def get_name(self):
        ''' returns the name 
        @param name: 
        '''
        return self.name
    
    def get_fun(self):
        ''' returns the function
        @return: function
        '''
        return self.fun

    def get_tuples(self):
        ''' returns the fields
        '''
        return self.ttuples

    def _get_columns(self):
        ''' private method returning the columns
        
        @return: returns the name of the columns
        '''
        
        # returns all fields of the corresponding named tuple
        return self.get_tuples()._fields

    def _get_type_of_colum(self, _name):
        ''' private method returning the type of a column
        '''
        
        return self.tsets[_name]

    def setup(self, _dryrun = 0):
        ''' setups the table within the database
        '''
        
        stmt = "CREATE TABLE {} (".format(self.name)
        for item in self._get_columns():
            
            stmt = stmt + item + " {},".format(self._get_type_of_colum(item))
        
        # leaving the for - loop from above, there is one colon to much, delete it!
        stmt = stmt[:-1] + ")"
        
        # send a small debugging information
        self.logger.debug("setup statement: '"+ stmt + "'")
        
        if _dryrun == 0:
            try:
                self.cursor.execute(stmt)
                self.conn.commit()
            except sqlite3.Error as e:
                self.logger.critical("An error occurred: {}".format(e.args[0]))
                return -1    
        
    
    def destroy(self, _dryrun = '0'):
        ''' destroy the table
        
        @param _dryrun: '1', the method does not take the sql execute 
            statement's path
        '''
        stmt = "DROP TABLE {}".format(self.name)
        
        # send a small debugging information
        self.logger.debug("setup statement: '"+ stmt + "'")
        
        if _dryrun == 0:
            self.cursor.execute(stmt)
            self.conn.commit()

    def _push(self, _args, _dryrun = 0):
        ''' generic push method
        
        @param _args:
        @param _dryrun: '1', the method does not take the sql execute 
            statement's path
            
        @return: 
        '''
        
        # initialize the variable
        stmt = "INSERT INTO {} (".format(self.name)
        
        # now, loop over the columns    
        for item in self._get_columns():
            if item == "id":
                continue
            stmt = stmt + item + ", "
         
        stmt = stmt[:-2] + ") values ("
        
        # loop over all columns
        for item in self._get_columns():
            if item == "id":
                continue
            stmt = stmt + "?,"
        
        # finalize the statement
        stmt = stmt[:-1] + ")"
        
        # push a message into the logger
        self.logger.debug(stmt + "{}".format(_args))

        # check, whether this is just a dry run
        if _dryrun == 0:
            try:
                self.cursor.execute(stmt, _args)
                self.conn.commit()
            except sqlite3.Error as e:
                self.logger.critical("An error occurred: {}".format(e.args[0]))
                return -1

    def _pop(self, _args, _dryrun = 0):
        ''' pops an entry from the table
        
        @param _args: 
        @param _dryrun: '1', the method does not take the sql execute 
            statement's path
        '''
        
                # initialize the variable
        stmt = "DELETE FROM {} WHERE ".format(self.name)
        
        # now, loop over the columns    
        for item in self._get_columns():
            if item == "id":
                continue
            stmt = stmt + item + " = ? and "

        # finalize the statement         
        stmt = stmt[:-4]
        
        # push a message into the logger
        self.logger.debug(stmt + "{}".format(_args))

        # check, whether this is just a dry run
        if _dryrun == 0:
            try:
                self.cursor.execute(stmt, _args)
                self.conn.commit()
                return 0
            except sqlite3.Error as e:
                self.logger.critical("An error occurred: {}".format(e.args[0]))
                return -1

    def _pop_all(self):
        ''' pops all entries from the table

        @param _cursor database cursor
        '''
        stmt = "SELECT * FROM {}".format(self.name)
        self.logger.debug(stmt)
        self.cursor.execute(stmt)

        entries = self.cursor.fetchall()
        for row in entries:
            self.logger.debug("deleting {}".format(row))
            
            # we do not expect to have the ID within the statement, hence
            # delete it
            self._pop(row[1:])
        
    def _select_matching_id(self):
        ''' selects an entry with a matching ID
        '''
        raise NotImplementedError
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def _get_all(self):
        ''' returns all entries
        '''
        entries=[]
        self.cursor.execute("select * from members")
        
        list_of_entries = self.cursor.fetchall()
        for row in list_of_entries:
            
            # we do not return the ID
            entries.append(row[1:])
        
        return entries

class c_bm_table_members(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's class constructor
        c_bm_tables.__init__(self, "members", None, _conn, _cursor, t_bm_members_l, s_bm_table_members)
        self.logger.debug("constructor")
    
    def push(self, _args):
        '''    pushes a new entry into 'members' table
        
        @param _args    either you give me a set, or a tuple
        
        @return: 
        '''
        
        # call generic push method 
        self._push(_args)

    def pop(self, _args):
        '''    pops a new entry into 'members' table
    
        @param _cursor   database cursor
        @param _name     member's name
        '''
        
        # call generic pop method
        self._pop(_args)
        
    def pop_all(self):
        ''' pops all entries from the table
        '''
        self._pop_all()
        
    def select_matching_id(self):
        ''' selects an entry with a matching ID
        '''
        raise NotImplementedError
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def show_all(self):
        for row in self.cursor.execute("select * from {}".format(self.name)):
            self.logger.debug(row)

    def get_all(self):
        '''
        '''
        return self._get_all()
    
    def pop_where_id(self, _cursor, _id):
        '''    pops a new entry into 'members' table
        
        @param _cursor   database cursor
        @param _name     member's name
        '''
        try:
            self.cursor.execute("DELETE FROM {} WHERE id=?".format(self.name), (_id,))
            self.conn.commit()
            return 0
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return -1

    def select_where_name_match(self, _name):
        '''   selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE name=?".format(self.name), (_name,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

    def update_where_id_match(self, _id):
        '''    selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE id=?".format(self.name), (_id,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

class c_bm_table_matter_of_expense(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's class constructor
        c_bm_tables.__init__(self, "matter_of_expense", None, _conn, _cursor, t_bm_matter_of_expenses_l, s_bm_table_matter_of_expenses)
        self.logger.debug("constructor")
    
    def push(self, _args):
        '''    pushes a new entry into 'members' table
        
        @param _args    either you give me a set, or a tuple
        
        @return: 
        '''
        
        # call generic push method 
        self._push(_args)

    def pop(self, _args):
        '''    pops a new entry into 'members' table
    
        @param _cursor   database cursor
        @param _name     member's name
        '''
        
        # call generic pop method
        self._pop(_args)
        
    def pop_all(self):
        ''' pops all entries from the table
        '''
        self._pop_all()
        
    def select_matching_id(self):
        ''' selects an entry with a matching ID
        '''
        raise NotImplementedError
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def show_all(self):
        for row in self.cursor.execute("select * from {}".format(self.name)):
            self.logger.debug(row)

    def get_all(self):
        '''
        '''
        return self._get_all()
    
    def pop_where_id(self, _cursor, _id):
        '''    pops a new entry into 'members' table
        
        @param _cursor   database cursor
        @param _name     member's name
        '''
        try:
            self.cursor.execute("DELETE FROM {} WHERE id=?".format(self.name), (_id,))
            self.conn.commit()
            return 0
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return -1

    def select_where_name_match(self, _name):
        '''   selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE name=?".format(self.name), (_name,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

class c_bm_table_groups_of_expenses(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's class constructor
        c_bm_tables.__init__(self, "groups_of_expenses", None, _conn, _cursor, t_bm_table_groups_of_expenses_l, s_bm_table_groups_of_expenses)
        self.logger.debug("constructor")
    
    def push(self, _args):
        '''    pushes a new entry into 'members' table
        
        @param _args    either you give me a set, or a tuple
        
        @return: 
        '''
        
        # call generic push method 
        self._push(_args)

    def pop(self, _args):
        '''    pops a new entry into 'members' table
    
        @param _cursor   database cursor
        @param _name     member's name
        '''
        
        # call generic pop method
        self._pop(_args)
        
    def pop_all(self):
        ''' pops all entries from the table
        '''
        self._pop_all()
        
    def select_matching_id(self):
        ''' selects an entry with a matching ID
        '''
        raise NotImplementedError
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def show_all(self):
        for row in self.cursor.execute("select * from {}".format(self.name)):
            self.logger.debug(row)

    def get_all(self):
        '''
        '''
        return self._get_all()
    
    def pop_where_id(self, _cursor, _id):
        '''    pops a new entry into 'members' table
        
        @param _cursor   database cursor
        @param _name     member's name
        '''
        try:
            self.cursor.execute("DELETE FROM {} WHERE id=?".format(self.name), (_id,))
            self.conn.commit()
            return 0
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return -1

    def select_where_name_match(self, _name):
        '''   selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE name=?".format(self.name), (_name,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

    def update_where_id_match(self, _id):
        '''    selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE id=?".format(self.name), (_id,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

class c_bm_table_invoice(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's class constructor
        c_bm_tables.__init__(self, "invoices", None, _conn, _cursor, t_bm_table_invoice_l, s_bm_table_invoice)
        self.logger.debug("constructor")
    
    def push(self, _args):
        '''    pushes a new entry into 'members' table
        
        @param _args    either you give me a set, or a tuple
        
        @return: 
        '''
        
        # call generic push method 
        self._push(_args)

    def pop(self, _args):
        '''    pops a new entry into 'members' table
    
        @param _cursor   database cursor
        @param _name     member's name
        '''
        
        # call generic pop method
        self._pop(_args)
        
    def pop_all(self):
        ''' pops all entries from the table
        '''
        self._pop_all()
        
    def select_matching_id(self):
        ''' selects an entry with a matching ID
        '''
        raise NotImplementedError
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def show_all(self):
        for row in self.cursor.execute("select * from {}".format(self.name)):
            self.logger.debug(row)

    def get_all(self):
        '''
        '''
        return self._get_all()
    
    def pop_where_id(self, _cursor, _id):
        '''    pops a new entry into 'members' table
        
        @param _cursor   database cursor
        @param _name     member's name
        '''
        try:
            self.cursor.execute("DELETE FROM {} WHERE id=?".format(self.name), (_id,))
            self.conn.commit()
            return 0
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return -1

    def select_where_matter_of_expense_match(self, _name):
        '''   selects a specnameific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE matter_of_expense=?".format(self.name), (_name,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

    def update_where_id_match(self, _id):
        '''    selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE id=?".format(self.name), (_id,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1
        
class c_bm_table_groups_of_members(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's class constructor
        c_bm_tables.__init__(self, "groups_of_members", None, _conn, _cursor, t_bm_table_groups_of_members_l, s_bm_table_groups_of_members)
        self.logger.debug("constructor")
    
    def push(self, _args):
        '''    pushes a new entry into 'members' table
        
        @param _args    either you give me a set, or a tuple
        
        @return: 
        '''
        
        # call generic push method 
        self._push(_args)

    def pop(self, _args):
        '''    pops a new entry into 'members' table
    
        @param _cursor   database cursor
        @param _name     member's name
        '''
        
        # call generic pop method
        self._pop(_args)
        
    def pop_all(self):
        ''' pops all entries from the table
        '''
        self._pop_all()
        
    def select_matching_id(self):
        ''' selects an entry with a matching ID
        '''
        raise NotImplementedError
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def show_all(self):
        for row in self.cursor.execute("select * from {}".format(self.name)):
            self.logger.debug(row)

    def get_all(self):
        '''
        '''
        return self._get_all()
    
    def pop_where_id(self, _cursor, _id):
        '''    pops a new entry into 'members' table
        
        @param _cursor   database cursor
        @param _name     member's name
        '''
        try:
            self.cursor.execute("DELETE FROM {} WHERE id=?".format(self.name), (_id,))
            self.conn.commit()
            return 0
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return -1

    def select_where_name_match(self, _name):
        '''   selects a specnameific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE name=?".format(self.name), (_name,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

    def update_where_id_match(self, _id):
        '''    selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE id=?".format(self.name), (_id,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1    

class c_bm_table_earnings(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's class constructor
        c_bm_tables.__init__(self, "earnings", None, _conn, _cursor, t_bm_table_earnings_l, s_bm_table_earnings)
        self.logger.debug("constructor")
    
    def push(self, _args):
        '''    pushes a new entry into 'members' table
        
        @param _args    either you give me a set, or a tuple
        
        @return: 
        '''
        
        # call generic push method 
        self._push(_args)

    def pop(self, _args):
        '''    pops a new entry into 'members' table
    
        @param _cursor   database cursor
        @param _name     member's name
        '''
        
        # call generic pop method
        self._pop(_args)
        
    def pop_all(self):
        ''' pops all entries from the table
        '''
        self._pop_all()
        
    def select_matching_id(self):
        ''' selects an entry with a matching ID
        '''
        raise NotImplementedError
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def show_all(self):
        for row in self.cursor.execute("select * from {}".format(self.name)):
            self.logger.debug(row)

    def get_all(self):
        '''
        '''
        return self._get_all()
    
    def pop_where_id(self, _cursor, _id):
        '''    pops a new entry into 'members' table
        
        @param _cursor   database cursor
        @param _name     member's name
        '''
        try:
            self.cursor.execute("DELETE FROM {} WHERE id=?".format(self.name), (_id,))
            self.conn.commit()
            return 0
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return -1

    def select_where_name_match(self, _name):
        '''   selects a specnameific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE name=?".format(self.name), (_name,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

    def update_where_id_match(self, _id):
        '''    selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE id=?".format(self.name), (_id,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1    

class c_bm_table_accounts(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's class constructor
        c_bm_tables.__init__(self, "accounts", None, _conn, _cursor, t_bm_table_accounts_l, s_bm_table_accounts)
        self.logger.debug("constructor")
    
    def push(self, _args):
        '''    pushes a new entry into 'members' table
        
        @param _args    either you give me a set, or a tuple
        
        @return: 
        '''
        
        # call generic push method 
        self._push(_args)

    def pop(self, _args):
        '''    pops a new entry into 'members' table
    
        @param _cursor   database cursor
        @param _name     member's name
        '''
        
        # call generic pop method
        self._pop(_args)
        
    def pop_all(self):
        ''' pops all entries from the table
        '''
        self._pop_all()
        
    def select_matching_id(self):
        ''' selects an entry with a matching ID
        '''
        raise NotImplementedError
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def show_all(self):
        for row in self.cursor.execute("select * from {}".format(self.name)):
            self.logger.debug(row)

    def get_all(self):
        '''
        '''
        return self._get_all()
    
    def pop_where_id(self, _cursor, _id):
        '''    pops a new entry into 'members' table
        
        @param _cursor   database cursor
        @param _name     member's name
        '''
        try:
            self.cursor.execute("DELETE FROM {} WHERE id=?".format(self.name), (_id,))
            self.conn.commit()
            return 0
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return -1

    def select_where_name_match(self, _name):
        '''   selects a specnameific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE name=?".format(self.name), (_name,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

    def update_where_id_match(self, _id):
        '''    selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE id=?".format(self.name), (_id,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1    

class c_bm_table_class(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's class constructor
        c_bm_tables.__init__(self, "class", None, _conn, _cursor, t_bm_table_class_l, s_bm_table_class)
        self.logger.debug("constructor")
    
    def push(self, _args):
        '''    pushes a new entry into 'members' table
        
        @param _args    either you give me a set, or a tuple
        
        @return: 
        '''
        
        # call generic push method 
        self._push(_args)

    def pop(self, _args):
        '''    pops a new entry into 'members' table
    
        @param _cursor   database cursor
        @param _name     member's name
        '''
        
        # call generic pop method
        self._pop(_args)
        
    def pop_all(self):
        ''' pops all entries from the table
        '''
        self._pop_all()
        
    def select_matching_id(self):
        ''' selects an entry with a matching ID
        '''
        raise NotImplementedError
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def show_all(self):
        for row in self.cursor.execute("select * from {}".format(self.name)):
            self.logger.debug(row)

    def get_all(self):
        '''
        '''
        return self._get_all()
    
    def pop_where_id(self, _cursor, _id):
        '''    pops a new entry into 'members' table
        
        @param _cursor   database cursor
        @param _name     member's name
        '''
        try:
            self.cursor.execute("DELETE FROM {} WHERE id=?".format(self.name), (_id,))
            self.conn.commit()
            return 0
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
            return -1

    def select_where_name_match(self, _name):
        '''   selects a specnameific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE name=?".format(self.name), (_name,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1

    def update_where_id_match(self, _id):
        '''    selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''   
        try:
            self.cursor.execute("SELECT id FROM {} WHERE id=?".format(self.name), (_id,))
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1    
          
class c_app(mod_logging_mkI_PYTHON.c_logging):
    ''' application, does not really do anything
    
    child class of c_logging
    '''
    
    def __init__(self):
        ''' constructor
        '''
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name + ".{}".format(g_program_suffix))
        return
    
    def run(self):
        ''' runs the main 
        '''
        self.logger.debug("application running")
        
        bm_database = c_bm_database()
        (conn, cursor) =  bm_database.connect()
        
        bm_table_members = c_bm_table_members(conn, cursor)
        bm_table_members.setup()
        
        # create an array in order to push data
        data = []
        data.append(t_bm_members_s(name = "test2", group_of_members = 1))
        data.append(t_bm_members_s(name = "test3", group_of_members = 1))
        data.append(t_bm_members_s(name = "test4", group_of_members = 1))
        data.append(t_bm_members_s(name = "test5", group_of_members = 1))
        
        # push data into the table
        self.logger.warn("pushing an array of data")
        for item in data:
            bm_table_members.push(item)
        
        # push a message into the logger that we will start to show it all
        self.logger.warn("show it all") 
        bm_table_members.show_all()

        # now, pop one after the other and show the entries in between
        self.logger.warn("pop one after the other")
        for item in data:
            bm_table_members.pop(item)
            bm_table_members.show_all()
        
        # push the data again into the table
        self.logger.warn("pushing an array of data")
        for item in data:
            bm_table_members.push(item)
        
        # show it all
        self.logger.warn("show it all")
        bm_table_members.show_all()
        
        # and pop it once
        self.logger.warn("pop all")
        bm_table_members.pop_all()
        
        # show it all
        self.logger.warn("show it all")
        bm_table_members.show_all()

        # use the getall functions in order to retrieve it
        self.logger.warn("pushing an array of data")
        for item in data:
            bm_table_members.push(item)

        entries = bm_table_members.get_all()
        for item in entries:
            self.logger.debug(item)
#         bm_table_members.destroy()
        
        bm_database.disconnect()
    
if __name__ == "__main__":
    # execute only if run as a script
    app = c_app()
    app.run()
