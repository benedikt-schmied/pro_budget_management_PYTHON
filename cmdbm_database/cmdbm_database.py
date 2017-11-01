#!/usr/bin/python3
# coding=latin-1

import sys
import sqlite3
import os
import argparse
import curses

def main():
    print("Hello World")
    
    while True:
        c = stdscr.getch()
        if c == ord('p'):
            PrintDocument()
        elif c == ord('q'):
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
    
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
    
    args = parser.parse_args()
    
    main()