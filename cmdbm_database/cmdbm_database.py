#!/usr/bin/python3
# coding=latin-1

import sys
import sqlite3
import os
import argparse
import curses
from curses import wrapper

def main(stdscr):
     
    while True:
        c = stdscr.getch()
        
        if c == ord('p'):
            stdscr.addstr(0,0, "printing", curses.A_BOLD)
            stdscr.refresh()
        elif c == ord('s'):
            stdscr.addstr(1,0, "plotting", curses.A_BOLD)
            stdscr.refresh()
        elif c == ord('q'):
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0

def build_terminal_session():

    curses.noecho()
    curses.cbreak()
    return

def restore_terminal_session(_src):
    curses.nocbreak()
    curses.echo()
    curses.endwin()

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
    
    parser = argparse.ArgumentParser(description='command line interface of database backend of bugdet management')
    parser.add_argument('user', default='admin', help='who is in charge of making changes or printing lists')
    
    args = parser.parse_args()
    stdscr = curses.initscr()
    wrapper(main)