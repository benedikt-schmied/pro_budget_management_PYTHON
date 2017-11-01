#!/usr/bin/python3
# coding=latin-1

import sys
import sqlite3
import os

import bm_database

def main():
    c=bm_database.setup_db()
    bm_database.push_into_members(c, "Horst", 1)
    bm_database.push_into_members(c, "Kevin", 1)
    bm_database.push_into_members(c, "Lolita", 1)
    bm_database.show_all_members(c)

if __name__ == "__main__":
    # execute only if run as a script
    print("standalone")
    main()