#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
sys.path.append('./../bm_export')
from bm_globals import *
import mod_logging_mkI_PYTHON
import sqlite3
from collections import namedtuple

g_program_suffix = "bm_database"

''' database definitions
first, there comes a namedtuple in order to ease data retrivals
second, there is a dictionary which holds the data types for each column
'''

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
                return 0
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
                return 0
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

        # finalize the statement                 return 0
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
        
    def _select_matching_id(self, _id):
        ''' selects an entry with a matching ID
        '''#         bm_database.pop_from_members(d, _name = name)
        stmt = "SELECT * FROM {} WHERE id = {}".format(self.name, _id)
        self.logger.debug(stmt)
        self.cursor.execute(stmt)

        entries = self.cursor.fetchone()
            
        # we do not expect to have the ID within the statement, hence
        # delete it
        return entries
    
    def show_matching_id(self):
        ''' shows an entry with a matching ID
        '''
        raise NotImplementedError

    def _get_all(self):
        ''' returns all entries
        '''
        entries=[]
        self.cursor.execute("select * from {}".format(self.name))
        
        list_of_entries = self.cursor.fetchall()
        for row in list_of_entries:
            
            # we do not return the ID
            entries.append(row[1:])
        
        return entries
    
    def _get_all_l(self):
        ''' returns all entries
        '''
        self.cursor.execute("select * from {}".format(self.name))
        
        list_of_entries = self.cursor.fetchall()
        return list_of_entries
    
    def _update_matching_id(self, _id, _args):
        '''    selects a specific entry where the name matches
        
        the statement looks similar to:
        Update table_name
        SET column1 = value1, column2 = value2, ...
        WHERE condition
        
        @param _cursor database cursor
        '''   
        
                # we need a list in order to pass the arguments as an array
        args = []
        
        for item in self.ttuples._fields:
            if item == "id":
                continue
            args.append(getattr(_args, item))
        
        try:
            stmt = "Update {} SET ".format(self.name)
            
            # now, loop over the columns    
            cnt = 0
            for item in self._get_columns():
                if item == "id":
                    continue
                
                stmt = stmt + item + " = '{}', ".format(args[cnt])
                
                # increment the looop counter
                cnt = cnt + 1
            
            stmt = stmt[:-2] + " "
            
            # append the id
            stmt = stmt + "WHERE id = {}".format(_id)
            
            self.logger.critical(stmt)
            
            # now, run this statement
            self.cursor.execute(stmt)
            self.conn.commit()
            return 0
        except sqlite3.Error as e:
            print("An error occrred: ", e.args[0])
            return -1
        
    def _prepare_export_all(self):
        ''' takes advantage of the exporting class in order to export all
        items
        '''
        headings = []
        
        for item in self.ttuples._fields:
            hstr = ""
            for subitem in item.split("_"):
                hstr = hstr + subitem + " "
            hstr = hstr[:-1]
            headings.append(hstr)
            
        data = self._get_all_l()
        
        results = []
        for _ in range(0, len(self.ttuples._fields)):
            results.append(" ")
        
        return (self.name, headings, data, results)
