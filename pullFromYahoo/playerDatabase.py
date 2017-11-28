#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:30:49 2017

@author: tbrady
"""

import sqlite3

sqlite_file = '/Users/tbrady/Documents/GitHub/saltystats/pullFromYahoo/db/sql/playerDatabase.db'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

table_name = 'players'
index_column = '*'
match_column = 'player_id'
match_value = '30199'



#c.execute('UPDATE {tn} set {mc}=0 WHERE {ic}={pid}'.\
#        format(tn=table_name, mc=match_column, ic=index_column, pid=player_id))




#c.execute('SELECT {ic} from {tn} WHERE name="Tom Brady"'.\
#        format(ic=index_column, tn=table_name, mc=match_column, mv=match_value))
#all_rows = c.fetchall()


def closeDatabase():
    conn.close()

def selectEntryFromTable(table_name = table_name, index_column = index_column, \
                         match_column = match_column, match_value=match_value):
    match_value=str(match_value)
    if match_value.isnumeric():
        c.execute('SELECT {ic} FROM {tn} WHERE {mc}={mv}'.\
            format(ic=index_column, tn=table_name, mc=match_column, mv=match_value))
    else: 
        c.execute('SELECT {ic} FROM {tn} WHERE {mc}="{mv}"'.\
            format(ic=index_column, tn=table_name, mc=match_column, mv=match_value))
    all_rows = c.fetchall()
    print(('SELECT {ic} FROM {tn} WHERE {mc}={mv}'.\
            format(ic=index_column, tn=table_name, mc=match_column, mv=match_value)))
    return all_rows[0]


def getTableColumnNames(table_name):
    c.execute('PRAGMA table_info({tn})'.\
              format(tn=table_name))
    tmp = c.fetchall()

    return tmp

def updateTableEntry(table_name = table_name, index_column = index_column, \
                     match_column = match_column, match_value=match_value,num=0):   
    match_value=str(match_value)
    c.execute('UPDATE {tn} SET {ic}={num} WHERE {mc}={mv}'.\
        format(ic=index_column, tn=table_name, mc=match_column, mv=match_value, num=num))




    

#print('{}'.format(data))


