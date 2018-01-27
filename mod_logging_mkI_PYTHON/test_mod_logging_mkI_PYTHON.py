#!/usr/bin/python3
# coding=latin-1

'''
creation date
author 

objectives:

logging module for various purposes 
'''

# imports
import mod_logging_mkI_PYTHON
import time

g_test_logname = "test_logging"

class c_test_main_class(mod_logging_mkI_PYTHON.c_logging):

    def __init__(self):
        '''
        '''
        
        # initialize the base class
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_test_logname)
        
        # create an instance of the sub class
        self.subclass = c_test_sub_class()
        
    def run(self):
        '''
        '''
        self.subclass.run()
        self.logger.critical("main class running")
        

class c_test_sub_class(mod_logging_mkI_PYTHON.c_sublogging):
    
    logname = "subclass"
    
    def __init__(self):
        '''
        '''
        
        # initialize the base class
        mod_logging_mkI_PYTHON.c_sublogging.__init__(self, g_test_logname + "." + self.logname)
        
    def run(self):
        self.logger.critical("submodule running")

if __name__ == "__main__":
    
    test_main_class = c_test_main_class()
    test_main_class.run()
    
    
    

