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
import os # for sys calls
import argparse
from collections import namedtuple
sys.path.append('./../mod_logging_mkI_PYTHON')
sys.path.append('./../_pro')
import mod_logging_mkI_PYTHON
from bm_globals import *
import time

test_t = namedtuple("test_t", ["account", "amount"])

class c_bm_export_tex(mod_logging_mkI_PYTHON.c_sublogging):

    def __init__(self, _subject, _intro, _headings, _data, _results, _outro):
        ''' constructor which fills up the internal variables
        '''
        
        mod_logging_mkI_PYTHON.c_sublogging.__init__(self, g_program_name + ".tex")
        
        self.subject    = _subject
        self.intro      = _intro
        self.headings   = _headings
        self.data       = _data
        self.results    = _results
        self.outro      = _outro
        self.section_item = ""

    def _write(self, _str):

        self.section_item = self.section_item + _str 

    def getitems(self):
        '''
        returns the final 'tex' - string
        
        @return: '-1' is something is wrong
        '''
        self._create_table()
        
        subject = ""
        for item in self.subject.split("_"):
            subject = subject + item + " "
        subject = subject[:-1]
        
        texstr = "\\section{" + subject + "}\n"
        texstr = texstr + self.intro + "\\\\\n\\\\\n"
        texstr = texstr + self.section_item
        texstr = texstr + "\\\\\n\\\\\n"
        texstr = texstr + self.outro + "\n"
        return texstr

    def _create_table(self):
                # we need to make sure, that the dimension of date and heading is equal
        if (len(self.data[0]) != len(self.headings) != len(self.results)):
            self.logger.warn("length is unequal, quitting")
            return -1

        cstr = ""
        for _ in range(0, len(self.headings)):
            cstr = cstr + "l"

        self._write("\\begin{tabular}{" + cstr + "} \\toprule \n");
        
        # now, create the headings
        hstr = ""
        for heading in self.headings:
            hstr = hstr + "{} &".format(heading)
        
        hstr = hstr[:-2] + "\\\\ \\midrule\n" 
        self._write(hstr)

        dstr = ""
        
        for row in self.data:
            for column in row:
                dstr = dstr + "{} &".format(column)
            dstr = dstr[:-2] + "\\\\\n"
            self._write(dstr)
            dstr = ""
        
        estr = ""
        for _ in range(0, len(self.headings)):
            estr = estr + "&"
        
        estr = estr[:-1]
        
        self._write(estr + "\\\\ \midrule\n")
        
        # now, create the headings
        rstr = ""
        for result in self.results:
            rstr = rstr + "{} &".format(result)
        
        rstr = rstr[:-2] + "\\\\ \n" 
        self._write(rstr)
        
        self._write("\\bottomrule\n \\end{tabular}\n ");
        
class c_app(mod_logging_mkI_PYTHON.c_logging):
    
    def __init__(self):
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name)
        return
    
    def run(self):
        l_bm_export_tex = c_bm_export_tex(
            _subject = "sql_to_tex",
            _intro  = "intro text", 
            _headings = ["column1", "column2", "column3"], 
            _data = [
                ["11", "12", "13"],
                ["21", "22", "23"],
                ["31", "32", "33"],
                ["41", "42", "43"],
                ["51", "52", "53"],
                ], 
            _results = ["42", "43", "444"],
            _outro = "outro text")
        ret = l_bm_export_tex.getitems()
        if ret != -1:
            self.logger.info(ret)
        
if __name__ == "__main__":
    # execute only if run as a script
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()
    if args.user == "admin":
        l_app = c_app()
        l_app.run()
    