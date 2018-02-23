#!/usr/bin/python3 
# coding=latin-1
import sys

sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')

from enum import Enum

class test_result(Enum):
    failed = -1
    succeeded = 0

class c_test():
    ''' comprises multiple test cases
    '''
    def __init__(self):
        self.test_cases = []
        
    
    def append(self, _class):
        ''' append a class
        '''
        self.test_cases.append(_class)
        
    def run(self):
        
        # loop over all test cases and run its functions
        for item in self.test_cases:
            if (item.fun() != 0):
                print("test ", item.name, " failed")
                return

class c_test_case():
    ''' 
    \brief test case class
    '''
    
    def __init__(self, _name, _fun):
        ''' the constructor
        '''
        self.fun = _fun # function
        self.name = _name

    def test_assert(self, _expected, _actual):
        ''' assert statement
        '''
        if (_expected != _actual):
            return
        
    