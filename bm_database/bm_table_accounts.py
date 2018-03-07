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

# accounts
t_bm_table_accounts_l = namedtuple('t_bm_table_accounts_l', [\
    'id', 'name' \
    ])

t_bm_table_accounts_s = namedtuple('t_bm_table_accounts_s', [\
    'name' \
    ])

s_bm_table_accounts = {'id': 'integer primary key', 'name': 'text unique'}

class c_bm_table_accounts(c_bm_tables):
    ''' budget management database's member table
    '''
    
    def __init__(self, _conn, _cursor):
        ''' constructor
        '''
        
        # call the father's accounts constructor
        c_bm_tables.__init__(self, "accounts", None, _conn, _cursor, t_bm_table_accounts_l, s_bm_table_accounts)
        self.logger.debug("constructor")
    
    def push(self, _args):
        '''    pushes a new entry into 'members' table
        
        @param _args    either you give me a set, or a tuple
        
        @return: 
        '''
        
        # call generic push method 
        return self._push(_args)

    def pop(self, _args):
        '''    pops a new entry into 'members' table
    
        @param _cursor   database cursor
        @param _name     member's name
        '''
        
        # call generic pop method
        args = _args[1:]
        return self._pop(args)
        
    def pop_all(self):
        ''' pops all entries from the table
        '''
        return self._pop_all()
        
    def select_matching_id(self, _id):
        ''' selects an entry with a matching ID
        '''
        return t_bm_table_accounts_l._make(self._select_matching_id(_id))
    
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def get_all(self):
        ''' fetches all entries from the database
        '''
        entries = []
        for row in self._get_all():
            entries.append(t_bm_table_accounts_s._make(row))
        return entries
    
    def get_all_l(self):
        ''' fetches all entries from the database
        '''
        entries = []
        for row in self._get_all_l():
            entries.append(t_bm_table_accounts_l._make(row))
        return entries

    def show_all(self):
        ''' shows all entries
        '''
        
        entries = self.get_all()
        for row in entries:
            
            # start the string that shall be printed
            pstr = "\t"
            cnt = 0
            
            for item in t_bm_table_accounts_s._fields:
                
                pstr = pstr + item
                pstr = pstr + " = "
                pstr = pstr + str(row[cnt])
                pstr = pstr + ", "
                
                # increment the counter variable
                cnt = cnt + 1
            
            # delete the last two characters
            pstr = pstr[:-2]
            
            print(pstr)
            
    def show_all_l(self):
        ''' shows all entries
        '''
        
        entries = self._get_all_l()
        for row in entries:
            
            # start the string that shall be printed
            pstr = "\t"
            cnt = 0
            
            for item in t_bm_table_accounts_l._fields:
                
                pstr = pstr + item
                pstr = pstr + " = "
                pstr = pstr + str(row[cnt])
                pstr = pstr + ", "
                
                # increment the counter variable
                cnt = cnt + 1
            
            # delete the last two characters
            pstr = pstr[:-2]
            
            print(pstr)
    
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

    def update_matching_id(self, _id, _args):
        '''    selects a specific entry where the name matches
        
        @param _cursor database cursor
        '''
                    
        self._update_matching_id(_id, _args)

    def _test_routines(self):
        
        self.setup()
        
        data = []
        data.append(t_bm_table_accounts_s(name = "test"))
        data.append(t_bm_table_accounts_s(name = "test2"))
        data.append(t_bm_table_accounts_s(name = "test3"))
        data.append(t_bm_table_accounts_s(name = "test4"))
        
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
          
