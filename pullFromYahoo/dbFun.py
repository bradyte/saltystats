#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 07:50:04 2017

@author: tbrady
"""
 
#from func import *



import csv
import glob
path = '/Users/tbrady/Documents/GitHub/saltystats/pullFromYahoo/dbfiles/raw/*.txt'


files = glob.glob(path)


p    = []


for file in files:
    with open(file) as f:
        reader = csv.reader(f, delimiter="\t")
        arr = list(reader)
        for i in range(0,len(arr)):
            if arr[i][1] != 'None':
                p.append([int(arr[i][0]),arr[i][1],arr[i][2]])
#                print(         str(arr[i][0]) + '\t' \
#                             + str(arr[i][1]) + '\t' \
#                             + str(arr[i][2]))
p.sort()

O = []
qb = []
rb = []
wr = []
te = []
k  = []
for i in range(0,len(p)):
    O.append([p[i][0], p[i][1], p[i][2]])
    if   p[i][1] == 'QB':
        qb.append([p[i][0], p[i][1], p[i][2]])
    elif p[i][1] == 'RB':
        rb.append([p[i][0], p[i][1], p[i][2]])
    elif p[i][1] == 'WR':
        wr.append([p[i][0], p[i][1], p[i][2]])
    elif p[i][1] == 'TE':
        te.append([p[i][0], p[i][1], p[i][2]])
    elif p[i][1] == 'K':
        k.append( [p[i][0], p[i][1], p[i][2]])









#filePath        = '/Users/tbrady/drive/sw/json/yahoo/oauth2.json'
#oauthToken      = beginOauth2Session(filePath)
#
#season          = 2017
#league_id       = 470610
#team_id         = 1
#week            = 1
#roster_size     = 15
#
#start = 31000
#filename = str('namedb'+str(start)+'_'+str(start+999)+'.txt')
#
#with open(filename, 'w') as output:
#    for player_id in range(start,start+1000):
#        arr = doesPlayerExist(season, player_id, week, oauthToken)
#        output.write(  str(arr[0]) + '\t' \
#                     + str(arr[1]) + '\t' \
#                     + str(arr[2]) + '\n')
#        print(         str(arr[0]) + '\t' \
#                     + str(arr[1]) + '\t' \
#                     + str(arr[2]))