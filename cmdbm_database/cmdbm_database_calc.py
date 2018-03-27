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
from collections import namedtuple
import bm_table_matter_of_expenses
import bm_table_earnings
import bm_table_accounts
sys.path.append('./../bm_database')
sys.path.append('./../mod_logging_mkI_PYTHON')
import sqlite3
import os
import argparse
from bm_database import *
import mod_logging_mkI_PYTHON
from cmdmenu import *
from cmdbm_database_setup import *
import time
from cmdbm_database_tex import *

test_t = namedtuple("test_t", ["account", "amount"])

class c_menu_calc(mod_logging_mkI_PYTHON.c_logging):
    ''' print menu
    '''
     
    def __init__(self):
         
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name + ".calc")
         
        # we need a variable which holds the main menu    
        self.menu_calc = []
        self.menu_calc.append(c_menu_items('te', 'total_expenses', 'give me the total expenses', self.total_expenses))
        self.menu_calc.append(c_menu_items('ti', 'total income', 'total earnings', self.total_earnings))
        self.menu_calc.append(c_menu_items('sd', 'saldo', 'saldo', self.saldo))
        self.menu_calc.append(c_menu_items('tr', 'transfer', 'transfer', self.transfer))
        self.menu_calc.append(c_menu_items('ep', 'personal expenses person', 'give me the personal', self.personal_expenses))
        
        return
    
    def total_earnings(self):
        ''' calculate the total earnings
        '''
        
        # push a message to the logger
        self.logger.warn('total earnings')
        
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
        
        bm_table_earnings = c_bm_table_earnings(conn, cursor)
        bm_table_earnings.show_all_l()
        
        earnings = 0
        for item in bm_table_earnings.get_all():
            print("\t\t name = {}, account = {}, amount = {}".format(item.name, item.account, item.amount))
            earnings = earnings + item.amount

        print("\t\t total earnings = {}".format(earnings))
        
        # now, disconnect again
        bm_database.disconnect()
        return earnings
    
    def total_expenses(self):
        ''' calc the total expenses
        '''
        
        # push a message to the logger
        self.logger.warn('total expenses') 
        
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
        
        # create a member class
        bm_table_matter_of_expenses = c_bm_table_matter_of_expenses(conn, cursor)
        bm_table_matter_of_expenses.show_all_l()
        
        amount = 0
        
        for item in bm_table_matter_of_expenses.get_all():
            print("\t\t name = {}, amount = {}, frequency = {}".format(item.name, item.amount, item.frequency))
            
            if item.frequency > 4:
                divider = item.frequency / 4
                amount = amount + (item.amount / divider)
            else:
                amount = amount + (item.amount)
         
        print("\t\t total expenses = {}".format(amount))
        
        # now, disconnect again
        bm_database.disconnect()
        return amount

    def saldo(self):
        ''' calc the total expenses
        '''
        expenses = self.total_expenses()
        earnings = self.total_earnings()
        
        print("\t\t total income - total expenses = {} - {} = {}".format(earnings, expenses, earnings - expenses))
    
     
    def expenses_of_person(self, _personidx):
        ''' expenses
        '''
        
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
        
        stmt = "SELECT name, amount, frequency\
            FROM matter_of_expenses \
            WHERE originator = {}".format(_personidx)
        
        cursor.execute(stmt)
        
        l_sum = 0
        for item in cursor.fetchall():
            print(item)
            
            if int(item[2]) > 4: 
                l_sum = l_sum + float(item[1]) / item[2] / 4
            else:
                l_sum = l_sum + float(item[1])
    
        print("Person {} l_summe {}".format(_personidx, l_sum))
        sys.stdout.flush()
        
        # now, disconnect again
        bm_database.disconnect()
        return l_sum
    
    def personal_expenses(self):
        ''' expenses tanja
        '''
        
        expenses = self.total_expenses()
        earnings = self.total_earnings()
        
        tanja_expenses = self.expenses_of_person(1)
        benedikt_expenses = self.expenses_of_person(2)
        
        diff = abs(tanja_expenses - benedikt_expenses)
        
        print("diff {}".format(diff))
        
        spare = earnings - expenses
        print("spare {}".format(spare))
        
        spare2 = 0.5 * (spare - diff) 
        
        print("tanja expenses + diff + topping = {} + {}  + {} =  {}".format(tanja_expenses, diff, spare2/2, tanja_expenses + diff + spare2/2))
        print("benedikt expenses + diff + topping = {} + {}  + {} =  {}".format(benedikt_expenses, 0, spare2/2, benedikt_expenses + 0 + spare2/2))
        
        print("spare {}".format(spare2))
        
        sys.stdout.flush()
        
    def transfer(self):
        ''' first, select all accounts that receive money
        then, subtract from the incoming money the amount which is said to
        be transferred from this account
        then, transfer the residual amount to other accounts, start with the
        first account, go to the next in the list
        '''
        
        # push a message to the logger
        self.logger.warn('transfer')
        
        # now, connect to the database
        bm_database = c_bm_database()
        (conn, cursor) = bm_database.connect()
        
        bm_table_earnings = c_bm_table_earnings(conn, cursor)
        bm_table_accounts = c_bm_table_accounts(conn, cursor)
        
        # fetch all accounts
        aclist = bm_table_accounts.get_all_l()
        
        # receiver accounts
        reclist = []
        
        # transmitter list
        tralist = []
            
        # loop over the earnings list
        for ac in aclist:
            
            # check, whether this is account has got a posi
            stmt = "SELECT name, amount, frequency \
                    FROM matter_of_expenses \
                    WHERE account = {}".format(ac.id)
            
            # take the db cursor and fetch the entries
            cursor.execute(stmt)
                        
            # reset the l_sum variable
            l_sum = 0
            
            # fetch the entries
            for it in cursor.fetchall():
                
                print(it)
                
                if it[2] > 4:
                    l_sum = l_sum + float(it[1]) / it[2] * 4
                else:
                    l_sum = l_sum + float(it[1])
            
            stmt = "SELECT name, amount \
                FROM earnings \
                WHERE account = {}".format(ac.id)
            
            cursor.execute(stmt)
            income = cursor.fetchone()
            print(income)
            if income != None:
            
                # calculate the residual money
                residual = float(income[1]) - l_sum
            else:
                residual = -l_sum
        
            # this account receives money
            if residual <= 0:
                reclist.append(test_t(ac.name, -residual))
            else: # this account transmits money
                tralist.append(test_t(ac.name, residual))

        # now, start sorting both lists
        reclist = sorted(reclist, key=lambda test_t: test_t.amount, reverse = True)
        tralist = sorted(tralist, key=lambda test_t: test_t.amount, reverse = True)

        print("transfer list {}".format(tralist))
        print("receiver list {}".format(reclist))

        test_t2 = namedtuple("test_t2", ["from_account", "to_account", "amount"])
        
        transfers = []
        
        # loop over all transmit accounts and define the transfers
        for tra in tralist:
            
            togive = tra.amount
            cpyreclist = reclist
            cnt = 0
            for rec in cpyreclist:
                
                print(togive)
                
                if (togive - rec.amount) > 0:
                    togive = togive - rec.amount
                    # modify the entry and push it bak
                    del(reclist[cnt])
                    transfers.append(test_t2(tra.account, rec.account, rec.amount))
                else:
                    # modify the entry and push it bak
                    reclist[cnt] = test_t(rec.account, togive)
                    transfers.append(test_t2(tra.account, rec.account, togive))
                    break
                cnt = cnt + 1
                
        for tr in transfers:
            print(tr)
        '''
        at this point, we have fetched all accounts that encounter incomings
        and we now, how much is left on this accounts. 
        Now, I would suggest to start with all the account, that has got the 
        highest dept
        '''

        sys.stdout.flush()
        
        # now, disconnect again
        bm_database.disconnect()
        return None

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

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()