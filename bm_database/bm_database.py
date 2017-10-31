#!/usr/bin/python3 
# coding=latin-1

import sys
import sqlite3
import os
import eyed3

def test_code(c):
    push_into_artist(c, "Absolute Beginner")
    push_into_artist(c, "Fettes Brot")
    push_into_artist(c, "Beginner")
    push_into_artist(c, "Beginner")
    show_all_artists(c)
    push_into_album(c, get_artist(c, "Beginner"), "Blast Action Hero", "2003")
    push_into_album(c, get_artist(c, "Fettes Brot"), "3 ist ne Party", "2015")
    push_into_album(c, get_artist(c, "Absolute Beginner"), "Bambule", "1998")
    show_all_albums(c)
    push_into_tracks(c, get_album(c, "3 ist ne Party", get_artist(c, "Fettes Brot")), "Jein", 1, 192, "C:/")
    push_into_tracks(c, get_album(c, "Blast Action Hero", get_artist(c, "Beginner")), "Faeule", 1, 192, "C:/")
    show_all_tracks(c)
# gehe erst durch die komplette Ordner - Struktur, manipuliere gegebenfalls
# einträge, das heißt ausschließlich den Pfad
# kopiere dann alle Einträge der Datenbank an einen neuen Ort
# Setzen eines Pfads
# falls eine wav datei vorhanden ist, wandle diese in eine flac - datei
def main():
    print(">>> starting up the music converter <<<")
    c=setup_db()
    setup_eyed3()
    fm=eyed3.load("01_Absolute_Beginner-Das_Boot.mp3")
    push_into_artist(c, fm.tag.artist)
    push_into_album(c, get_artist(c, fm.tag.artist), fm.tag.album, 1997)
    push_into_tracks(c, get_album(c, fm.tag.album, get_artist(c, fm.tag.artist)), fm.tag.title, fm.tag.track_num[0], 192, "C:/")
    show_all_albums(c)
    show_all_artists(c)
    show_all_tracks(c)
    fm=eyed3.load("09_Absolute_Beginner-Chili-Chil_BÃ¤ng_BÃ¤ng.mp3")
    push_into_artist(c, fm.tag.artist)
    push_into_album(c, get_artist(c, fm.tag.artist), fm.tag.album, 1997)
    push_into_tracks(c, get_album(c, fm.tag.album, get_artist(c, fm.tag.artist)), fm.tag.title, fm.tag.track_num[0], 192, "C:/")
    show_all_albums(c)
    show_all_artists(c)
    show_all_tracks(c)

def setup_db():
    print("    setting up tnamehe database")
    conn = sqlite3.connect("dbmusic.db")
    c=conn.cursor()
    
    for i in range(0,3):
        try:
            if i == 0:
                c.execute("CREATE TABLE artists (id integer primary key, name text unique)")
            elif i == 1:
                c.execute("CREATE TABLE track (id integer primary key, album integer, name text, number integer, rate integer, bakpath text)")
            elif i == 2:
                c.execute("CREATE TABLE album (id integer primary key, artist integer, name text, date txt)")
                
        except :
            print("    this table exists already")
    return c
            

def push_into_artist(cursor, name):
    print("    pushing artist")
    try:
        cursor.execute("INSERT INTO artists(name) values (?)", (name,))
    except:
        print("    dublicate artist encountered")      
        
def push_into_album(cursor, artist, name, date):
    print("    pushing album")
    cursor.execute("INSERT INTO album(artist, name, date) values (?,?,?)", (artist, name, date,))
    print("    dublicate album encountered")

def push_into_tracks(cursor, album, name, number, rate, bakpath):
    print("    pushing track")
    cursor.execute("INSERT INTO track(album, name, number, rate, bakpath) values (?,?,?,?,?)", (album, name, number, rate, bakpath,))


def show_all_artists(cursor):
    for row in cursor.execute("select * from artists"):
        print(row)

def show_all_albums(cursor):
    for row in cursor.execute("select * from album"):
        print(row)
        
def show_all_tracks(cursor):
    for row in cursor.execute("select * from track"):
        print(row)

def get_artist(cursor, name):
    print("    searching for artist")
    try:
        cursor.execute("select artists.id from artists where artists.name=? ", (name,))
        r=cursor.fetchone()
        type(r)
        r[0]
        return r[0]
    except:
        print("    did not find anything")
        return

def get_album(cursor, name, artist):
    print("    searching for album")

    cursor.execute("select album.id from album where album.name=? and album.artist=? ", (name,artist,))
    r=cursor.fetchone()
    type(r)
    r[0]
    return r[0]

def setup_eyed3():
    print("    setting up the eyed3 plugin")


    
if __name__ == "__main__":
    # execute only if run as a script
    main()
