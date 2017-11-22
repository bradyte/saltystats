#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 07:50:04 2017

@author: tbrady
"""
import league_settings as ls
from func import *
import nfl_info as nfl
import csv
import glob
path = '/Users/tbrady/Documents/GitHub/saltystats/pullFromYahoo/dbfiles/raw/*.txt'

#
#start = 31000
#filename = str('namedb'+str(start)+'_'+str(start+999)+'.txt')
#
#with open(filename, 'w') as output:
#    for player_id in range(start,start+1000):
#        arr = getPlayerInfo(season, player_id, week, oauthToken)
#        output.write(  str(arr[0]) + '\t' \
#                     + str(arr[1]) + '\t' \
#                     + str(arr[2]) + '\n')
#        print(         str(arr[0]) + '\t' \
#                     + str(arr[1]) + '\t' \
#                     + str(arr[2]))


#files = glob.glob(path)
#p    = []
#
#for file in files:
#    with open(file) as f:
#        reader = csv.reader(f, delimiter="\t")
#        arr = list(reader)
#        for i in range(0,len(arr)):
#            if arr[i][1] != 'None':
#                p.append([int(arr[i][0]),arr[i][1],arr[i][2]])
##                print(         str(arr[i][0]) + '\t' \
##                             + str(arr[i][1]) + '\t' \
##                             + str(arr[i][2]))
#p.sort()
#
#O = []
#qb = []
#rb = []
#wr = []
#te = []
#k  = []
#for i in range(0,len(p)):
#    O.append([p[i][0], p[i][1], p[i][2]])
#    if   p[i][1] == 'QB':
#        qb.append([p[i][0], p[i][1], p[i][2]])
#    elif p[i][1] == 'RB':
#        rb.append([p[i][0], p[i][1], p[i][2]])
#    elif p[i][1] == 'WR':
#        wr.append([p[i][0], p[i][1], p[i][2]])
#    elif p[i][1] == 'TE':
#        te.append([p[i][0], p[i][1], p[i][2]])
#    elif p[i][1] == 'K':
#        k.append( [p[i][0], p[i][1], p[i][2]])








#arr = wr
#

away    = False
player  = nfl.qb[1]
opp     = nfl.schedule[int(player[1])][int(ls.week)]
if opp[0] == '@':
    opp = int(opp[1:])
    away = True
    # away game
    

oppinfo = nfl.dst[int(opp)]
#for j in range(0,len(arr)):
#    arr[j] = doesPlayerExist(season, arr[j][0], week, oauthToken)
#
#
#with open('/Users/tbrady/Documents/GitHub/saltystats/pullFromYahoo/dbfiles/wrpids.csv','w') as resFile:
#    writ = csv.writer(resFile,delimiter=',')
#    writ.writerows(arr)


