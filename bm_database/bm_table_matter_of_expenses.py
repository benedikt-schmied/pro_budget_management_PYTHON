#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
from bm_globals import *
import mod_logging_mkI_PYTHON
import sqlite3
from collections import namedtuple
from bm_tables import *


''' database definitions
first, there comes a namedtuple in order to ease data retrivals
second, there is a dictionary which holds the data types for each column
'''

# matter of expenses 
t_bm_matter_of_expenses_l = namedtuple('t_bm_matter_of_expenses_l', [ \
    'id', 'name', 'originator', 'originator_class', 'provider', 'provider_class', \
    'groups_of_expenses', 'amount', 'frequency', 'account'\
    ])

t_bm_table_matter_of_expenses_s = namedtuple('t_bm_table_matter_of_expenses_s', [ \
    'name', 'originator', 'originator_class', 'provider', 'provider_class', \
    'groups_of_expenses', 'amount', 'frequency', 'account'\
    ])

s_bm_table_matter_of_expenses = {'id': 'integer primary key', 'name': 'text', 'originator_class': 'integer', 'originator': 'integer', \
    'provider_class': 'integer', 'provider': 'integer', 'groups_of_expenses': 'integer', 'amount': 'float', \
    'frequency': 'integer', 'account': 'integer'}


class c_bm_table_matter_of_expenses(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's class constructor
        c_bm_tables.__init__(self, "matter_of_expenses", None, _conn, _cursor, t_bm_matter_of_expenses_l, s_bm_table_matter_of_expenses)
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
    
    def _test_routines(self):
        
        self.setup()
        
        data = []
        data.append(t_bm_table_matter_of_expenses_s(name = "test", originator = 1, originator_class = 1, provider = 1, provider_class = 1, 
                                              groups_of_expenses = 1, amount = 1.4, frequency = 1, account = 1))
        data.append(t_bm_table_matter_of_expenses_s(name = "test2", originator = 1, originator_class = 1, provider = 1, provider_class = 1, 
                                              groups_of_expenses = 1, amount = 1.4, frequency = 1, account = 1))
        
        self.logger.warn("pushing an array of data")
        for item in data:
            self.push(item)
        
        # push a message into the logger that we will start to show it all
        self.logger.warn("show it all") 
        self.show_all()

        # now, pop one after the other and show the entries in between
        self.logger.warn("pop one after the other")
        for item in data:
            self.pop(item)
            self.show_all()
        
        # push the data again into the table
        self.logger.warn("pushing an array of data")
        for item in data:
            self.push(item)
        
        # show it all
        self.logger.warn("show it all")
        self.show_all()
        
        # and pop it once
        self.logger.warn("pop all")
        self.pop_all()
        
        # show it all
        self.logger.warn("show it all")
        self.show_all()

        # use the getall functions in order to retrieve it
        self.logger.warn("pushing an array of data")
        for item in data:
            self.push(item)

        entries = self.get_all()
        for item in entries:
            self.logger.debug(item)