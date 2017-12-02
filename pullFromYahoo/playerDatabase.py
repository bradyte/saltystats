#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 10:30:49 2017

@author: tbrady
"""

import sqlite3
import settings as ls
import csv

sqliteFile      = 'db/sql/playerDatabase.db'
playerFile      = 'db/csv/playerInfo.csv'

conn            = sqlite3.connect(sqliteFile)
#conn.row_factory = lambda cursor, row: row[0]
c               = conn.cursor()

table_name      = 'stats_s2017w1'
index_column    = '*'
match_column    = 'player_id'
match_value     = '3288'


with open(playerFile, 'r') as f:
    reader  = csv.reader(f)
    pInfo   = list(reader)

#table_name = 'stats_s' + str(ls.season) + 'w' + str(ls.week) 
#pdb.createSQLTable(table_name)
##pdb.executeSQL('DROP TABLE IF EXISTS {tn}'.format(tn=table_name))
#ids = pdb.selectAllPlayerIDs()
##idx = 1001
##inc = 200
#for i in range(len(ids)):
#    if int(ids[i]) < 100000: # protect against defense ids
#        [statsArray, fpts] = yq.updatePlayerStatsQuery(ids[i], table_name)
#        perc = ((i+1)/len(ids))*100
#        print('\r{:.3f}% '.format(perc),end='')
#        time.sleep(0.1)


def getSeasonPerformanceSQL(table_name = table_name, index_column = index_column, \
                         match_column = match_column, match_value=match_value):
    stats = []
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    for i in range(1,ls.week):
        table_name = 'stats_s' + str(ls.season) + 'w' + str(i)
        c.execute('SELECT {ic} FROM {tn} WHERE {mc}={mv}'.\
            format(ic=index_column, tn=table_name, mc=match_column, mv=match_value))
        stats.append([i,c.fetchall()[0]])
    return stats
        
def getWeeklyPositionPerformanceSQL(index_column, match_column, match_value, week):
    table_name = 'stats_s' + str(ls.season) + 'w' + str(week)
    arr = c.execute('SELECT {ic} FROM {tn} WHERE {mc}="{mv}" AND active=1'.\
        format(ic=index_column, tn=table_name, mc=match_column, mv=match_value)).fetchall()
    arr.sort(reverse=True)
    return arr

def getWeeklyPlayerPerformanceSQL(index_column, match_column, match_value, week):
    try:
        table_name = 'stats_s' + str(ls.season) + 'w' + str(week)
        tmp = c.execute('SELECT {ic} FROM {tn} WHERE {mc}="{mv}" AND active=1'.\
            format(ic=index_column, tn=table_name, mc=match_column, mv=match_value)).fetchall()
        return tmp[0]
    except IndexError:
        return 'null'

#def checkForBYESQL(table_name = table_name, index_column = index_column, \
#                         match_column = match_column, match_value=match_value, week):
#    index_column = statName[84] # get team_id
#    table_name = 'stats_s' + str(ls.season) + 'w' + str(week)
#    
#    conn.row_factory = lambda cursor, row: row[0]
#    c = conn.cursor()
#    
#    c.execute('SELECT {ic} FROM {tn} WHERE {mc}={mv}'.\
#            format(ic=index_column, tn=table_name, mc=match_column, mv=match_value))
#    
#    
#    
#    
#    table_name = 'schedule_s2017'
    

def executeSQL(sql_string):
    c.execute(sql_string)


def closeDatabase():
    conn.commit()
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
#    print(('SELECT {ic} FROM {tn} WHERE {mc}={mv}'.\
#            format(ic=index_column, tn=table_name, mc=match_column, mv=match_value)))

    return all_rows[0]

def selectAllPlayerIDs(table_name = table_name, index_column = index_column):
    c.execute('SELECT {ic} FROM {tn}'.format(ic=index_column, tn=table_name))
    all_rows = c.fetchall()
    return [x[83] for x in all_rows]


def getTableColumnNames(table_name):
    c.execute('PRAGMA table_info({tn})'.format(tn=table_name))
    tmp = c.fetchall()

    return tmp

def updateTableEntry(table_name = table_name, index_column = index_column, \
                     match_column = match_column, match_value=match_value,num=0):   
    match_value=str(match_value)
    c.execute('UPDATE {tn} SET {ic}={num} WHERE {mc}={mv}'.\
        format(ic=index_column, tn=table_name, mc=match_column, mv=match_value, num=num))

def createNewRowSQL(table_name): 
    c.execute('INSERT INTO {tn}(\
        {d00}, {d01}, {d02}, {d03}, {d04},\
        {d05}, {d06}, {d07}, {d08}, {d09},\
        {d10}, {d11}, {d12}, {d13}, {d14},\
        {d15}, {d16}, {d17}, {d18}, {d19},\
        {d20}, {d21}, {d22}, {d23}, {d24},\
        {d25}, {d26}, {d27}, {d28}, {d29},\
        {d30}, {d31}, {d32}, {d33}, {d34},\
        {d35}, {d36}, {d37}, {d38}, {d39},\
        {d40}, {d41}, {d42}, {d43}, {d44},\
        {d45}, {d46}, {d47}, {d48}, {d49},\
        {d50}, {d51}, {d52}, {d53}, {d54},\
        {d55}, {d56}, {d57}, {d58}, {d59},\
        {d60}, {d61}, {d62}, {d63}, {d64},\
        {d65}, {d66}, {d67}, {d68}, {d69},\
        {d70}, {d71}, {d72}, {d73}, {d74},\
        {d75}, {d76}, {d77}, {d78}, {d79},\
        {d80}, {d81}, {d82},\
        {d83}, {d84}, {d85}, {d86}, {d87}, {d88}) \
        VALUES(\
        0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,\
        0,0,0,\
        {pid},{team_id},"{pos}","{name}","{team_abbr}",0)'.\
        format(tn=table_name,
        d00=ls.statName[0],  d01=ls.statName[1],  d02=ls.statName[2],  d03=ls.statName[3],  d04=ls.statName[4], 
        d05=ls.statName[5],  d06=ls.statName[6],  d07=ls.statName[7],  d08=ls.statName[8],  d09=ls.statName[9], 
        d10=ls.statName[10], d11=ls.statName[11], d12=ls.statName[12], d13=ls.statName[13], d14=ls.statName[14], 
        d15=ls.statName[15], d16=ls.statName[16], d17=ls.statName[17], d18=ls.statName[18], d19=ls.statName[19], 
        d20=ls.statName[20], d21=ls.statName[21], d22=ls.statName[22], d23=ls.statName[23], d24=ls.statName[24], 
        d25=ls.statName[25], d26=ls.statName[26], d27=ls.statName[27], d28=ls.statName[28], d29=ls.statName[29], 
        d30=ls.statName[30], d31=ls.statName[31], d32=ls.statName[32], d33=ls.statName[33], d34=ls.statName[34], 
        d35=ls.statName[35], d36=ls.statName[36], d37=ls.statName[37], d38=ls.statName[38], d39=ls.statName[39], 
        d40=ls.statName[40], d41=ls.statName[41], d42=ls.statName[42], d43=ls.statName[43], d44=ls.statName[44], 
        d45=ls.statName[45], d46=ls.statName[46], d47=ls.statName[47], d48=ls.statName[48], d49=ls.statName[49], 
        d50=ls.statName[50], d51=ls.statName[51], d52=ls.statName[52], d53=ls.statName[53], d54=ls.statName[54], 
        d55=ls.statName[55], d56=ls.statName[56], d57=ls.statName[57], d58=ls.statName[58], d59=ls.statName[59], 
        d60=ls.statName[60], d61=ls.statName[61], d62=ls.statName[62], d63=ls.statName[63], d64=ls.statName[64], 
        d65=ls.statName[65], d66=ls.statName[66], d67=ls.statName[67], d68=ls.statName[68], d69=ls.statName[69], 
        d70=ls.statName[70], d71=ls.statName[71], d72=ls.statName[72], d73=ls.statName[73], d74=ls.statName[74], 
        d75=ls.statName[75], d76=ls.statName[76], d77=ls.statName[77], d78=ls.statName[78], d79=ls.statName[79], 
        d80=ls.statName[80], d81=ls.statName[81], d82=ls.statName[82], d83=ls.statName[83], d84=ls.statName[84],
        d85=ls.statName[85], d86=ls.statName[86], d87=ls.statName[87], d88=ls.statName[88],
        pid=pInfo[0][0],     team_id=pInfo[0][1],     pos=pInfo[0][2],    name=pInfo[0][3], team_abbr=pInfo[0][4]))
    
def createSQLTable(table_name):
    c.execute('CREATE TABLE IF NOT EXISTS "{tn}" ( \
        {d00} INTEGER, {d01} INTEGER, {d02} INTEGER, {d03} INTEGER, {d04} INTEGER,  \
        {d05} INTEGER, {d06} INTEGER, {d07} INTEGER, {d08} INTEGER, {d09} INTEGER,  \
        {d10} INTEGER, {d11} INTEGER, {d12} INTEGER, {d13} INTEGER, {d14} INTEGER,  \
        {d15} INTEGER, {d16} INTEGER, {d17} INTEGER, {d18} INTEGER, {d19} INTEGER,  \
        {d20} INTEGER, {d21} INTEGER, {d22} INTEGER, {d23} INTEGER, {d24} INTEGER,  \
        {d25} INTEGER, {d26} INTEGER, {d27} INTEGER, {d28} INTEGER, {d29} INTEGER,  \
        {d30} INTEGER, {d31} INTEGER, {d32} INTEGER, {d33} INTEGER, {d34} INTEGER,  \
        {d35} INTEGER, {d36} INTEGER, {d37} INTEGER, {d38} INTEGER, {d39} INTEGER,  \
        {d40} INTEGER, {d41} INTEGER, {d42} INTEGER, {d43} INTEGER, {d44} INTEGER,  \
        {d45} INTEGER, {d46} INTEGER, {d47} INTEGER, {d48} INTEGER, {d49} INTEGER,  \
        {d50} INTEGER, {d51} INTEGER, {d52} INTEGER, {d53} INTEGER, {d54} INTEGER,  \
        {d55} INTEGER, {d56} INTEGER, {d57} INTEGER, {d58} INTEGER, {d59} INTEGER,  \
        {d60} INTEGER, {d61} INTEGER, {d62} INTEGER, {d63} INTEGER, {d64} INTEGER,  \
        {d65} INTEGER, {d66} INTEGER, {d67} INTEGER, {d68} INTEGER, {d69} INTEGER,  \
        {d70} INTEGER, {d71} INTEGER, {d72} INTEGER, {d73} INTEGER, {d74} INTEGER,  \
        {d75} INTEGER, {d76} INTEGER, {d77} INTEGER, {d78} INTEGER, {d79} INTEGER,  \
        {d80} INTEGER, {d81} INTEGER, {d82} INTEGER, \
        {d83} INTEGER, {d84} INTEGER, {d85} TEXT, {d86} TEXT, {d87} TEXT, {d88} REAL)'.\
        format(tn=table_name,
        d00=ls.statName[0],  d01=ls.statName[1],  d02=ls.statName[2],  d03=ls.statName[3],  d04=ls.statName[4], 
        d05=ls.statName[5],  d06=ls.statName[6],  d07=ls.statName[7],  d08=ls.statName[8],  d09=ls.statName[9], 
        d10=ls.statName[10], d11=ls.statName[11], d12=ls.statName[12], d13=ls.statName[13], d14=ls.statName[14], 
        d15=ls.statName[15], d16=ls.statName[16], d17=ls.statName[17], d18=ls.statName[18], d19=ls.statName[19], 
        d20=ls.statName[20], d21=ls.statName[21], d22=ls.statName[22], d23=ls.statName[23], d24=ls.statName[24], 
        d25=ls.statName[25], d26=ls.statName[26], d27=ls.statName[27], d28=ls.statName[28], d29=ls.statName[29], 
        d30=ls.statName[30], d31=ls.statName[31], d32=ls.statName[32], d33=ls.statName[33], d34=ls.statName[34], 
        d35=ls.statName[35], d36=ls.statName[36], d37=ls.statName[37], d38=ls.statName[38], d39=ls.statName[39], 
        d40=ls.statName[40], d41=ls.statName[41], d42=ls.statName[42], d43=ls.statName[43], d44=ls.statName[44], 
        d45=ls.statName[45], d46=ls.statName[46], d47=ls.statName[47], d48=ls.statName[48], d49=ls.statName[49], 
        d50=ls.statName[50], d51=ls.statName[51], d52=ls.statName[52], d53=ls.statName[53], d54=ls.statName[54], 
        d55=ls.statName[55], d56=ls.statName[56], d57=ls.statName[57], d58=ls.statName[58], d59=ls.statName[59], 
        d60=ls.statName[60], d61=ls.statName[61], d62=ls.statName[62], d63=ls.statName[63], d64=ls.statName[64], 
        d65=ls.statName[65], d66=ls.statName[66], d67=ls.statName[67], d68=ls.statName[68], d69=ls.statName[69], 
        d70=ls.statName[70], d71=ls.statName[71], d72=ls.statName[72], d73=ls.statName[73], d74=ls.statName[74], 
        d75=ls.statName[75], d76=ls.statName[76], d77=ls.statName[77], d78=ls.statName[78], d79=ls.statName[79], 
        d80=ls.statName[80], d81=ls.statName[81], d82=ls.statName[82], d83=ls.statName[83], d84=ls.statName[84],
        d85=ls.statName[85], d86=ls.statName[86], d87=ls.statName[87], d88=ls.statName[88]))
        
    for i in range(len(pInfo)):    
        c.execute('INSERT INTO {tn}(\
            {d00}, {d01}, {d02}, {d03}, {d04},\
            {d05}, {d06}, {d07}, {d08}, {d09},\
            {d10}, {d11}, {d12}, {d13}, {d14},\
            {d15}, {d16}, {d17}, {d18}, {d19},\
            {d20}, {d21}, {d22}, {d23}, {d24},\
            {d25}, {d26}, {d27}, {d28}, {d29},\
            {d30}, {d31}, {d32}, {d33}, {d34},\
            {d35}, {d36}, {d37}, {d38}, {d39},\
            {d40}, {d41}, {d42}, {d43}, {d44},\
            {d45}, {d46}, {d47}, {d48}, {d49},\
            {d50}, {d51}, {d52}, {d53}, {d54},\
            {d55}, {d56}, {d57}, {d58}, {d59},\
            {d60}, {d61}, {d62}, {d63}, {d64},\
            {d65}, {d66}, {d67}, {d68}, {d69},\
            {d70}, {d71}, {d72}, {d73}, {d74},\
            {d75}, {d76}, {d77}, {d78}, {d79},\
            {d80}, {d81}, {d82},\
            {d83}, {d84}, {d85}, {d86}, {d87}, {d88}) \
            VALUES(\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,0,0,0,0,0,0,0,\
            0,0,0,\
            {pid},{team_id},"{pos}","{name}","{team_abbr}",0)'.\
            format(tn=table_name,
            d00=ls.statName[0],  d01=ls.statName[1],  d02=ls.statName[2],  d03=ls.statName[3],  d04=ls.statName[4], 
            d05=ls.statName[5],  d06=ls.statName[6],  d07=ls.statName[7],  d08=ls.statName[8],  d09=ls.statName[9], 
            d10=ls.statName[10], d11=ls.statName[11], d12=ls.statName[12], d13=ls.statName[13], d14=ls.statName[14], 
            d15=ls.statName[15], d16=ls.statName[16], d17=ls.statName[17], d18=ls.statName[18], d19=ls.statName[19], 
            d20=ls.statName[20], d21=ls.statName[21], d22=ls.statName[22], d23=ls.statName[23], d24=ls.statName[24], 
            d25=ls.statName[25], d26=ls.statName[26], d27=ls.statName[27], d28=ls.statName[28], d29=ls.statName[29], 
            d30=ls.statName[30], d31=ls.statName[31], d32=ls.statName[32], d33=ls.statName[33], d34=ls.statName[34], 
            d35=ls.statName[35], d36=ls.statName[36], d37=ls.statName[37], d38=ls.statName[38], d39=ls.statName[39], 
            d40=ls.statName[40], d41=ls.statName[41], d42=ls.statName[42], d43=ls.statName[43], d44=ls.statName[44], 
            d45=ls.statName[45], d46=ls.statName[46], d47=ls.statName[47], d48=ls.statName[48], d49=ls.statName[49], 
            d50=ls.statName[50], d51=ls.statName[51], d52=ls.statName[52], d53=ls.statName[53], d54=ls.statName[54], 
            d55=ls.statName[55], d56=ls.statName[56], d57=ls.statName[57], d58=ls.statName[58], d59=ls.statName[59], 
            d60=ls.statName[60], d61=ls.statName[61], d62=ls.statName[62], d63=ls.statName[63], d64=ls.statName[64], 
            d65=ls.statName[65], d66=ls.statName[66], d67=ls.statName[67], d68=ls.statName[68], d69=ls.statName[69], 
            d70=ls.statName[70], d71=ls.statName[71], d72=ls.statName[72], d73=ls.statName[73], d74=ls.statName[74], 
            d75=ls.statName[75], d76=ls.statName[76], d77=ls.statName[77], d78=ls.statName[78], d79=ls.statName[79], 
            d80=ls.statName[80], d81=ls.statName[81], d82=ls.statName[82], d83=ls.statName[83], d84=ls.statName[84],
            d85=ls.statName[85], d86=ls.statName[86], d87=ls.statName[87], d88=ls.statName[88],
            pid=pInfo[i][0],     team_id=pInfo[i][1],     pos=pInfo[i][2],    name=pInfo[i][3], team_abbr=pInfo[i][4]))

    
    




