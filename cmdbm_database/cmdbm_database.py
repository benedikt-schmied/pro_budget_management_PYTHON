#!/usr/bin/python3
# coding=latin-1

'''
creation date
author 

objectives:

small command line interface that lets you insert basic
information in each table, that lets you search within
a table and which prints human readable information 
'''

import sys
import sqlite3
import os
import argparse
import bm_database
import mod_logging_mkI_PYTHON

class c_menu_items():
    
    def __init__(self, _cmd = "n", _name = "none", _text = "no text", _fun = quit):
        self.cmd = _cmd
        self.name = _name
        self.help_text = _text
        self.fun = _fun    
        
    def set_function(self, _fun):
        self.fun = _fun
        
    def get_function(self):
        return self.fun
    
    def set_help_text(self, _text):
        self.help_text = _text
        
    def get_help_text(self):
        return self.help_text
    
    def set_name(self, _name):
        self.name = _name
        
    def get_name(self):
        return self.name
    
    def set_cmd(self, _cmd):
        self.cmd = _cmd
        
    def get_cmd(self):
        return self.cmd
    
class c_menu_help():
    ''' help menu
    '''
    
    def __init__(self):
        return
    
    def run(self):
        return

class c_menu_print(mod_logging_mkI_PYTHON.c_logging):
    ''' print menu
    '''
    
    def __init__(self):
        
        mod_logging_mkI_PYTHON.c_logging.__init__(self, 'cmd')
        
        # we need a variable which holds the main menu    
        self.menu_print = []
        self.menu_print.append(c_menu_items('at', 'all tables', 'print all tables', self.all_tables))
        self.menu_print.append(c_menu_items('me', 'members', 'print the member table', self.members))
        self.menu_print.append(c_menu_items('ex', 'matter of expense', 'matter of expense', self.matter_of_expense))  
        self.menu_print.append(c_menu_items('in', 'invoices', 'invoices', self.invoices))
        self.menu_print.append(c_menu_items('gm', 'groups of members', 'groups of members', self.groups_of_members))
        self.menu_print.append(c_menu_items('ge', 'groups of expenses', 'groups of expenses', self.groups_of_expenses))
        self.menu_print.append(c_menu_items('ea', 'earnings', 'earnings', self.earnings))
        self.menu_print.append(c_menu_items('ac', 'accounts', 'accounts', self.accounts))
        self.menu_print.append(c_menu_items('cl', 'classes', 'classes', self.classes))
        return
    
    def all_tables(self):
        self.logger.warn('all tables')
        self.members()
        self.matter_of_expense()
        self.invoices()
        self.groups_of_members()
        self.groups_of_expenses()
        self.earnings()
        self.accounts()
        self.classes()
        return
    
    def members(self):
        ''' print the members entries
        '''
        
        # push a message to the logger
        self.logger.warn('members')
        
        # now, connect to the database
        d = bm_database.connect()
        
        # fetch the entries
        entries = bm_database.get_entries_members(d)
        
        # show an introduction line
        print("\t\t ~~~ members")
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, name = {}, group = {}".format(cnti[0], cnti[1], cnti[2]))

        # disconnect again
        bm_database.disconnect(d)
        return 
    
    def matter_of_expense(self):
        ''' print the matter of expense entries
        
        '''
        
        # push a message to the logger
        self.logger.warn('matter of expense')
        
        d = bm_database.connect()
        entries = bm_database.get_entries_matter_of_expense(d)
        
        # show an introduction line
        print("\t\t ~~~ matter of expense")
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, name = {}, originator = {}, provider = {}, groups of expenses = {}, amount = {}, frequency = {}, account = {}".format(
                cnti[0], cnti[1], cnti[2], cnti[3], cnti[4], cnti[5], cnti[6], cnti[7]))

        bm_database.disconnect(d)
        return
    
    def invoices(self):
        ''' print the invoices entries
        '''
        
        # push a message into the logger
        self.logger.warn('invoices')
        
        # show an introduction line
        print("\t\t ~~~ invoices")
        
        # now, connect to the database
        d = bm_database.connect()
        
        # fetch the entries
        entries = bm_database.get_entries_invoices(d)
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, name = \t{}".format(cnti[0], cnti[1]))

        # disconnect again
        bm_database.disconnect(d)
        return 
    
    def groups_of_members(self):
        ''' print the group of members entries
        '''
        
        # push a message into the logger
        self.logger.warn('groups of members')
        
        # show an introduction line
        print("\t\t ~~~ groups of members")
        
        # now, connect to the database
        d = bm_database.connect()
        
        # fetch the entries
        entries = bm_database.get_entries_groups_of_members(d)
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, name = {}".format(cnti[0], cnti[1]))

        # disconnect again
        bm_database.disconnect(d)
        return    
    
    
    def groups_of_expenses(self):
        ''' print the group of expenses entries
        '''
        
        # push a message into the logger
        self.logger.warn('groups of expenses')
        
        # show an introduction line
        print("\t\t ~~~ groups of expenses")
        
        # now, connect to the database
        d = bm_database.connect()
        
        # fetch the entries
        entries = bm_database.get_entries_groups_of_expenses(d)
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> index = {}, name = {}".format(cnti[0], cnti[1]))

        # disconnect again
        bm_database.disconnect(d)
        return
    
    def earnings(self):
        ''' print the earnings entries
        '''
        
        # push a message into the logger
        self.logger.warn('earnings')
        
        # show an introduction line
        print("\t\t ~~~ earnings")
        
        # now, connect to the database
        d = bm_database.connect()
        
        # fetch the entries
        entries = bm_database.get_entries_earnings(d)
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, name = {}, account = {}, amount = {}".format(cnti[0], cnti[1], cnti[2], cnti[3]))

        # disconnect again
        bm_database.disconnect(d)
        return
    
    def accounts(self):
        ''' print the accounts entries
        '''
        
        # push a message into the logger
        self.logger.warn('accounts')
        
        # show an introduction line
        print("\t\t ~~~ accounts")        
        
        # now, connect to the database
        d = bm_database.connect()
        
        # fetch the entries
        entries = bm_database.get_entries_accounts(d)
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, account = {}".format(cnti[0], cnti[1]))

        # disconnect again
        bm_database.disconnect(d)
        return
    
    def classes(self):
        ''' print the classes entries
        '''
        
        # push a message into the logger
        self.logger.warn('classes')
        
        # show an introduction line
        print("\t\t ~~~ classes")        
        
        # now, connect to the database
        d = bm_database.connect()
        
        # fetch the entries
        entries = bm_database.get_entries_class(d)
        
        # run over all entries
        for cnti in entries:
            print("\t\t <-> \t index = {}, account = {}".format(cnti[0], cnti[1]))

        # disconnect again
        bm_database.disconnect(d)
        return
    
    def run(self):
        
        '''
        this is the main menu, you can either tell us to 
        print a table
        insert a new entry into a table
        or modify an entry within a table
        '''    
        self.logger.warn('running')
        while True:
            
            # first print the menu
            for cnt in range(0, len(self.menu_print)):
                print("{}\t{}".format(self.menu_print[cnt].get_cmd(), self.menu_print[cnt].get_help_text()))
            
            c = input("-->")
            
            print(c)

            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_print)):
                if c == self.menu_print[cnt].cmd:
                    print(self.menu_print[cnt].get_help_text())
                    self.menu_print[cnt].fun()
           
            if c =='q':
                break
    
    
    
class c_menu_insert():
    ''' print menu
    '''
    
    def __init__(self):
        
        mod_logging_mkI_PYTHON.c_logging.__init__(self, 'cmd')
        
        # we need a variable which holds the main menu    
        self.menu_insert = []
        self.menu_insert.append(c_menu_items('me', 'members', 'member table', self.members))
        self.menu_insert.append(c_menu_items('ex', 'matter of expense', 'matter of expense', self.matter_of_expense))  
        self.menu_insert.append(c_menu_items('in', 'invoices', 'invoices', self.invoices))
        self.menu_insert.append(c_menu_items('gm', 'groups of members', 'groups of members', self.groups_of_members))
        self.menu_insert.append(c_menu_items('ge', 'groups of expenses', 'groups of expenses', self.groups_of_expenses))
        self.menu_insert.append(c_menu_items('ea', 'earnings', 'earnings', self.earnings))
        self.menu_insert.append(c_menu_items('ac', 'accounts', 'accounts', self.accounts))
        self.menu_insert.append(c_menu_items('cl', 'classes', 'classes', self.classes))
        return
    
    def members(self):
        ''' insert into members entries
        '''
        
        # push a message to the logger
        self.logger.warn('members')
        
        # show all members so far
        menu_print = c_menu_print()
        menu_print.members()
        
        # ask the user for specific inputs        
        name = input("\t\t <--> name: ")
        
        # give the user some hints
        menu_print.groups_of_members()
        group = input("\t\t <--> group: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.push_into_members(d, name, group)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def matter_of_expense(self):
        ''' insert into matter of expense
        
        '''
        
        # push a message to the logger
        self.logger.warn('matter of expense')

        # print all existing entries
        menu_print = c_menu_print()
        menu_print.matter_of_expense()

        # ask the user for specific iputs
        name = input("\t\t <--> name: ")
        
        # print the members table in order to help the user
        menu_print.classes()
        menu_print.members()
        menu_print.groups_of_members()
        
        originator_class = input("\t\t <--> originator class: ")
        originator = input("\t\t <--> originator: ")
        provider_class = input("\t\t <--> provider class: ")
        provider = input("\t\t <--> provider: ")
        
        # print the groups of expenses table
        menu_print.groups_of_expenses()
        group = input("\t\t <--> group: ")
        amount = input("\t\t <--> amount: ")
        
        # tell the user to give the frequency in weeks
        frequency = input("\t\t <--> frequency [weeks]: ")
        
        # print the accounts table
        menu_print.accounts()
        account = input("\t\t <--> account: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.push_into_matter_of_expense(d, _name = name, _originator_class = originator_class, _originator = originator, _provider_class = provider_class, _provider = provider, _group = group, _amount = amount, _frequency = frequency, _account = account)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def invoices(self):
        ''' insert into the invoices table
        '''
        
        # push a message into the logger
        self.logger.warn('matter of invoices')
    
        # ask the user for specific inputs    
        matter_of_expense = input("\t\t <--> matter of expense: ")
        originator = input("\t\t <--> originator: ")
        date = input("\t\t <--> date: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.push_into_invoice(d, _matter_of_expense = matter_of_expense, _originator = originator, _date = date)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def groups_of_members(self):
        ''' insert into the group of members table
        '''
        
        # push a message into the logger
        self.logger.warn('groups of members')

        # print the members table in order to help the user
        menu_print = c_menu_print()
        menu_print.groups_of_members()

        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.push_into_groups_of_members(d, _name = name)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return   
    
    
    def groups_of_expenses(self):
        ''' insert into the group of expenses tables
        '''
        
        # push a message into the logger
        self.logger.warn('groups of expenses')

                # print the members table in order to help the user
        menu_print = c_menu_print()
        menu_print.groups_of_expenses()

        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.push_into_groups_of_expenses(d, _name = name)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return 
    
    def earnings(self):
        ''' print the earnings entries
        '''
        
        # push a message into the logger
        self.logger.warn('earnings')

        # print the members table in order to help the user
        menu_print = c_menu_print()
        menu_print.earnings()

        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
        
        # print the members table in order to help the user
        menu_print.accounts()
        
        account = input("\t\t <--> account: ")
        amount = input("\t\t <--> amount: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.push_into_earnings(d, _name = name, _account = account, _amount = amount)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def accounts(self):
        ''' print the accounts entries
        '''
        
        # push a message into the logger
        self.logger.warn('accounts')

        # print the members table in order to help the user
        menu_print = c_menu_print()
        menu_print.accounts()

        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.push_into_accounts(d, _name = name)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def classes(self):
        ''' print the classes entries
        '''
        
        # push a message into the logger
        self.logger.warn('classes')

        # ask the user for specific inputs
        name = input("\t\t <--> name: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.push_into_class(d, _name = name)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def run(self):
        
        '''
        this is the main menu, you can either tell us to 
        print a table
        insert a new entry into a table
        or modify an entry within a table
        '''    
        self.logger.warn('running')
        while True:
            
            # first print the menu
            for cnt in range(0, len(self.menu_insert)):
                print("{}\t{}".format(self.menu_insert[cnt].get_cmd(), self.menu_insert[cnt].get_help_text()))
            
            c = input("-->")
            
            print(c)

            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_insert)):
                if c == self.menu_insert[cnt].cmd:
                    print(self.menu_insert[cnt].get_help_text())
                    self.menu_insert[cnt].fun()
           
            if c =='q':
                break

class c_menu_delete():
    ''' print menu
    '''
    
    def __init__(self):
        
        mod_logging_mkI_PYTHON.c_logging.__init__(self, 'cmd')
        
        # we need a variable which holds the main menu    
        self.menu_delete = []
        self.menu_delete.append(c_menu_items('me', 'members', 'member table', self.members))
        self.menu_delete.append(c_menu_items('ex', 'matter of expense', 'matter of expense', self.matter_of_expense))  
        self.menu_delete.append(c_menu_items('in', 'invoices', 'invoices', self.invoices))
        self.menu_delete.append(c_menu_items('gm', 'groups of members', 'groups of members', self.groups_of_members))
        self.menu_delete.append(c_menu_items('ge', 'groups of expenses', 'groups of expenses', self.groups_of_expenses))
        self.menu_delete.append(c_menu_items('ea', 'earnings', 'earnings', self.earnings))
        self.menu_delete.append(c_menu_items('ac', 'accounts', 'accounts', self.accounts))
        self.menu_delete.append(c_menu_items('cl', 'classes', 'classes', self.classes))
        return
    
    def members(self):
        ''' insert into members entries
        '''
        
        # push a message to the logger
        self.logger.warn('members')
    
        # show the existing members
        menu_print = c_menu_print()
        menu_print.members()        
    
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
#         bm_database.pop_from_members(d, _name = name)
        bm_database.pop_from_members_where_id(d, _id = row)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def matter_of_expense(self):
        ''' insert into matter of expense
        
        '''
        
        # push a message to the logger
        self.logger.warn('matter of expense')
        
        # print the current items
        menu_print = c_menu_print()
        menu_print.matter_of_expense()
        
        # ask the user for specific inputs
        nr = input("\t\t id = ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.pop_from_matter_of_expense_where_id(d, _id = nr)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def invoices(self):
        ''' insert into the invoices table
        '''
        
        # push a message into the logger
        self.logger.warn('matter of invoices')

        # print the current items
        menu_print = c_menu_print()
        menu_print.invoices()
        
        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.pop_from_invoice_where_id(d, _id = row)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def groups_of_members(self):
        ''' insert into the group of members table
        '''
        
        # push a message into the logger
        self.logger.warn('groups of members')

        # print the current items
        menu_print = c_menu_print()
        menu_print.groups_of_members()

        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.pop_from_groups_of_members_where_id(d, _id = row)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return   
    
    
    def groups_of_expenses(self):
        ''' insert into the group of expenses tables
        '''
        
        # push a message into the logger
        self.logger.warn('groups of expenses')

        # print the current items
        menu_print = c_menu_print()
        menu_print.groups_of_expenses()

        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.pop_from_groups_of_expenses_where_id(d, _id = row)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return 
    
    def earnings(self):
        ''' print the earnings entries
        '''
        
        # push a message into the logger
        self.logger.warn('earnings')

        # print the current items
        menu_print = c_menu_print()
        menu_print.earnings()

        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.pop_from_earnings_where_id(d, _id = row)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def accounts(self):
        ''' print the accounts entries
        '''
        
        # push a message into the logger
        self.logger.warn('accounts')

        # print the current items
        menu_print = c_menu_print()
        menu_print.groups_of_expenses()

        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.pop_from_accounts_where_id(d, _id = row)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def classes(self):
        ''' print the classes entries
        '''
        
        # push a message into the logger
        self.logger.warn('classes')

        # print the current items
        menu_print = c_menu_print()
        menu_print.groups_of_expenses()

        # ask the user for specific inputs
        row = input("\t\t <--> id: ")
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        bm_database.pop_from_class_where_id(d, _id = row)
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def run(self):
        
        '''
        this is the main menu, you can either tell us to 
        print a table
        insert a new entry into a table
        or modify an entry within a table
        '''    
        self.logger.warn('running')
        while True:
            
            # first print the menu
            for cnt in range(0, len(self.menu_delete)):
                print("{}\t{}".format(self.menu_delete[cnt].get_cmd(), self.menu_delete[cnt].get_help_text()))
            
            c = input("-->")
            
            print(c)

            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_delete)):
                if c == self.menu_delete[cnt].cmd:
                    print(self.menu_delete[cnt].get_help_text())
                    self.menu_delete[cnt].fun()
           
            if c =='q':
                break
            
class c_menu_calc():
    ''' print menu
    '''
    
    def __init__(self):
        
        mod_logging_mkI_PYTHON.c_logging.__init__(self, 'cmd.warn')
        
        # we need a variable which holds the main menu    
        self.menu_calc = []
        self.menu_calc.append(c_menu_items('te', 'total_expenses', 'give me the total expenses', self.total_expenses))
        return
    
    def total_expenses(self):
        ''' calc the total expenses
        '''
        
        # push a message to the logger
        self.logger.warn('members')
        
        # connect to the database
        d = bm_database.connect()
        
        # now, push it to the table
        entries = []
        entries = bm_database.get_entries_matter_of_expense(d)
        amount = 0
        for item in entries:
            print("\t\t name = {}, amount = {}, frequency = {}".format(item[1], item[7], item[8]))
            
            if item[8] > 4:
                divider = item[8] / 4
                amount = amount + (item[7] / divider)
            else:
                amount = amount + (item[7])
        
        entries = []
        entries = bm_database.get_entries_earnings(d)
        earnings = 0
        for item in entries:
            print("\t\t name = {}, account = {}, amount = {}".format(item[1], item[2], item[3]))
            earnings = earnings + item[3]
        
        print("\t\t amount = {}, which means, we've got an income of {}, spare {}".format(amount, earnings, earnings - amount))
        
        # now, disconnect again
        bm_database.disconnect(d)
        return
    
    def run(self):
        
        '''
        this is the main menu, you can either tell us to 
        print a table
        insert a new entry into a table
        or modify an entry within a table
        '''    
        self.logger.warn('running')
        while True:
            
            # first print the menu
            for cnt in range(0, len(self.menu_calc)):
                print("{}\t{}".format(self.menu_calc[cnt].get_cmd(), self.menu_calc[cnt].get_help_text()))
            
            c = input("-->")
            
            print(c)

            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_calc)):
                if c == self.menu_calc[cnt].cmd:
                    print(self.menu_calc[cnt].get_help_text())
                    self.menu_calc[cnt].fun()
           
            if c =='q':
                break

class c_menu_top(mod_logging_mkI_PYTHON.c_logging):

    def __init__(self):
        
        mod_logging_mkI_PYTHON.c_logging.__init__(self, "cmd")
        
        # we need a variable which holds the main menu    
        self.menu_top = []
        self.menu_top.append(c_menu_items('p', 'print', 'printing something', self.menu_print))
        self.menu_top.append(c_menu_items('m', 'modify', 'modify an entry', self.menu_modify))
        self.menu_top.append(c_menu_items('i', 'insert', 'insert an entry', self.menu_insert))
        self.menu_top.append(c_menu_items('d', 'delete', 'delete an entry', self.menu_delete))
        self.menu_top.append(c_menu_items('c', 'calc', 'do some calculation', self.menu_calc))
        self.menu_top.append(c_menu_items('m', 'manual', 'manual', self.menu_manual))
        self.menu_top.append(c_menu_items('h', 'help', 'help menu', self.menu_help))
    
    def get_idx_by_cmd(self, _cmd):
        '''
        @param _cmd     command
        '''
        for cnt in range(0, self.menu_top):
            if _cmd == self.menu_top[cnt].cmd:
                return cnt
            return -1
        
    def menu_print(self, _midx):
        '''
        @param _midx    menu index
        '''
        menu_print = c_menu_print()
        menu_print.run()
        
    def menu_modify(self, _midx):
        '''
        @param _midx:
        '''    
        
    def menu_insert(self, _midx):
        '''
        @param _midx:
        '''
        menu_insert = c_menu_insert()
        menu_insert.run()

    def menu_delete(self, _midx):
        '''
        @param _midx:
        '''
        menu_delete = c_menu_delete()
        menu_delete.run()

    def menu_calc(self, _midx):
        '''
        @param _midx:
        '''
        menu_calc = c_menu_calc()
        menu_calc.run()

    def menu_manual(self, _midx):
        '''
        @param _midx:
        '''
        
        d = bm_database.connect()
        stmt = input("\t\t <--> typ the command: ")
        bm_database.manual_db_command(d, stmt)
        bm_database.disconnect(d)
        return
    
    def menu_help(self, _midx):
        '''
        @param 
        ''' 
        for item in self.menu_top:
            print("cmd ", item.get_cmd(), "\t", item.get_help_text())
    
    def run(self):
        '''
        @param _midx:
        '''  
        
        '''
        this is the main menu, you can either tell us to 
        print a table
        insert a new entry into a table
        or modify an entry within a table
        '''    
        
        # connect to the database 
        c = bm_database.connect() 
    
        # setup the database
        bm_database.setup_db(c)
        bm_database.disconnect(c)
        
        while True:
            
            for cnt in range(0, len(self.menu_top)):
                print("{}\t{}".format(self.menu_top[cnt].get_cmd(), self.menu_top[cnt].get_help_text()))
            
            c = input("-->")
            
            print(c)
            
            # no, we have to loop over the top menu items in 
            # order to find what we've got to docmd
            for cnt in range(0, len(self.menu_top)):
                if c == self.menu_top[cnt].cmd:
                    print(self.menu_top[cnt].get_help_text())
                    self.menu_top[cnt].fun(cnt)
           
            if c =='q':
                break
                

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()
    menu = c_menu_top()
    menu.run()