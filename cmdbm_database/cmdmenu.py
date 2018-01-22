#!/usr/bin/python3
# coding=latin-1

'''
creation date
author 

objectives:

menu
'''

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
                

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
