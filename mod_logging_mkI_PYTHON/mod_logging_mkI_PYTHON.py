#!/usr/bin/python3
# coding=latin-1

'''
creation date
author 

objectives:

logging module for various purposes 
'''

# imports
import logging
import time

class c_sublogging():
    
    def __init__(self, _logname):
        
        # create a logger
        self.logger = logging.getLogger(_logname)
        
        # create a handle for standard error stream and file output
        
        # add both handles to the logger
        self.logger.addHandler(logging.NullHandler())
         
    def testrun(self):
        self.logger.info("info message")
        self.logger.warn("warning message")
        self.logger.debug("debug message")
        self.logger.error("error message")
        self.logger.critical("critical message")

class c_logging():
    
    def __init__(self, _logname):
        
        # create a logger
        self.logger = logging.getLogger(_logname)
        
        # create a handle for standard error stream and file output
        self.stderrhdl  = logging.StreamHandler()
        #self.filehdl    = logging.FileHandler("{}_{}.log".format(_logname, time.strftime('%Y%m%d%H%M%S')))
        
        # set the debugging levels for both handlers
        self.stderrhdl.setLevel(logging.NOTSET)
        #self.filehdl.setLevel(logging.DEBUG)
        
        # create a formatter
        self.formatter = logging.Formatter('%(asctime)s %(name)-25s %(levelname)-10s %(message)s')
        
        # assign the formatter to both handles
        self.stderrhdl.setFormatter(self.formatter)
        #self.filehdl.setFormatter(self.formatter)
        
        # add both handles to the logger
        self.logger.addHandler(self.stderrhdl)
        #self.logger.addHandler(self.filehdl)
        
        self.logger.setLevel(35)
        
    def testrun(self):
        self.logger.info("info message")
        self.logger.warn("warning message")
        self.logger.debug("debug message")
        self.logger.error("error message")
        self.logger.critical("critical message")

if __name__ == "__main__":
    
    print("\t this {} module is not intended to run standalone".format(__name__))
    print("\t will quit after pushing various messages into the logger")
    
    logger = c_logging('test')
    logger.testrun()

