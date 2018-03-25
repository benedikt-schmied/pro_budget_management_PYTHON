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
from bm_export_tex import *
import time

test_t = namedtuple("test_t", ["account", "amount"])

class c_bm_export(mod_logging_mkI_PYTHON.c_sublogging):

    def __init__(self, _name, _date):
        ''' constructor which fills up the internal variables
        '''
        
        mod_logging_mkI_PYTHON.c_sublogging.__init__(self, g_program_name + ".tex")
        
        self.name       = _name
        self.date       = _date
    
    def push(self, _subject, _headings, _data, _results):
        ''' pushes new data into 
        '''
        return

    def write_to_file(self):
        '''
        writes to a file
        
        @return: '-1' is something is wrong
        '''
        filename = "{}_{}".format(self.name, self.date)

        with open(filename + ".tex", "wt") as texfile:

            # first, create the tex - specific stuff
            texfile.write("\\documentclass{scrartcl}\n");
            texfile.write("\\usepackage[paperwidth=40cm,paperheight=48cm]\
                {geometry}\n");
            texfile.write("\\usepackage{booktabs}\n");
            
            texfile.write("\\begin{document}\n");

            # loop over the subjects and write those data
            
            
            
            cstr = ""
            for _ in range(0, len(self.headings)):
                cstr = cstr + "l"

            texfile.write("\\begin{tabular}{" + cstr + "} \\toprule \n");
            
            # now, create the headings
            hstr = ""
            for heading in self.headings:
                hstr = hstr + "{} &".format(heading)
            
            hstr = hstr[:-2] + "\\\\ \\midrule\n" 
            texfile.write(hstr)

            dstr = ""
            
            for row in self.data:
                for column in row:
                    dstr = dstr + "{} &".format(column)
                dstr = dstr[:-2] + "\\\\\n"
                self.logger.warn(dstr)
                texfile.write(dstr)
                dstr = ""
            
            estr = ""
            for _ in range(0, len(self.headings)):
                estr = estr + "&"
            
            estr = estr[:-1]
            
            texfile.write(estr + "\\\\ \midrule\n")
            
            # now, create the headings
            rstr = ""
            for result in self.results:
                rstr = rstr + "{} &".format(result)
            
            rstr = rstr[:-2] + "\\\\ \n" 
            texfile.write(rstr)
            
            texfile.write("\\bottomrule\n \\end{tabular}\n ");
            
            texfile.write("\\end{document}");

            texfile.close()
        
        os.system("pdflatex " + filename + ".tex")
        os.system("okular " + filename + ".pdf")

class c_app(mod_logging_mkI_PYTHON.c_logging):
    
    def __init__(self):
        mod_logging_mkI_PYTHON.c_logging.__init__(self, g_program_name)
        return
    
    def run(self):
        l_bm_export = c_bm_export(
            _name = "sql_to_tex", 
            _date = time.strftime("%Y%m%d%H%M%s"), 
            _headings = ["column1", "column2", "column3"], 
            _data = [
                ["11", "12", "13"],
                ["21", "22", "23"],
                ["31", "32", "33"],
                ["41", "42", "43"],
                ["51", "52", "53"],
                ], 
            _results = ["42", "43", "444"])
        l_bm_export.write_to_file()
        
if __name__ == "__main__":
    # execute only if run as a script
     
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
                        
    args = parser.parse_args()
    if args.user == "admin":
        l_app = c_app()
        l_app.run()
    