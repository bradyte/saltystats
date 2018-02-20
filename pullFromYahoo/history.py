#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 07:01:27 2017

@author: tombrady
"""
import csv
import numpy as np
import glob
import matplotlib.pyplot as plt
import playerDatabase as pdb


def getHistArray(pos):
    table_name = 'position_' + pos
    index_column = 's201'

    vals = [[] for i in range(7)]

    labels = []
    for i in range(7):
        incol = index_column + str(i)
        tmp = pdb.executeSQL('SELECT {ic} FROM {tn} ORDER BY {ic} DESC'.format(
            tn = table_name, ic = incol))
        vals[i] = tmp
        labels.append(incol)
    vmean = np.mean(vals, axis=0)
    return vmean


#plt.figure(figsize=(8,6))
#for i in range(len(vals)):
#    plt.plot(vals[i],'.', label = labels[i][1:])
#
#
#plt.ylabel('Fantasy Points')
#plt.xlabel('Position Rank')
#plt.title('Fantasy Points vs Position Rank from 2010 - 2016')
#plt.legend()
#
#
#plt.figure(figsize=(8,6))
#vmean = np.mean(vals, axis=0)
#vstd = np.std(vals, axis=0)
#xrank = range(len(vmean))
#
#plt.errorbar(xrank, vmean, vstd, linestyle='None', marker='.')
#plt.ylabel('Fantasy Points')
#plt.xlabel('Position Rank')
#plt.title('Average Fantasy Points with St. Deviation from 2010 - 2016')
































#pos = 'wr'
#fpath = 'hist/'+pos+'/'
#if pos != 'ki':
#    scr = [0,0,0,0,0,0,0.04,4,-2,2,0,0.1,6,2,0.5,0.1,6,2,-2,0]
#else:
#    scr = [0,0,0,0,1,0,-1,0,0,3,0,3,0,3,0,4,0,5,0]
#
#tmp = 0
#idx = 0
#total = []
#
#tiers = []
#cumul = []
#
##f = 'qb2010.csv'
##for fname in glob.glob(fpath+'*.csv'):
#for k in range(2010,2017):
#    file = pos+str(k)+'.csv'
#    data = []
#    with open(fpath+file, 'r') as f:
#        reader  = csv.reader(f)
#        pInfo   = list(reader)
#
#
#    for i in range (1,len(pInfo)):
#        tmp = 0
#        for j in range(len(pInfo[0])):
#            if pInfo[i][j].isnumeric():
#                tmp += scr[j]*int(pInfo[i][j])/16
#        data.append(tmp)
#
#    data.sort(reverse=True)
#    total.append(data)
#    cumul.extend(data)
#
#cumul.sort(reverse=True)
#
#total = np.array(total)
#avg = total.mean(axis=0)
#
##for i in range(len(total)):
##    plt.plot(total[i],',')
##plt.plot(avg,'.')
##plt.hist(cumul[:210],bins=21)
#plt.show()
#k = 30
#inc = 10
#for i in range(len(total)):
#    tmp += np.sum(total[i][k:k+inc])
#
#
#mean = tmp/(int(len(total)*inc))

#table_name = 'position_'+pos
#
#pdb.executeSQL('DROP TABLE IF EXISTS {tn}'.format(tn=table_name))
#pdb.executeSQL('CREATE TABLE IF NOT EXISTS position_{p}(s2010 integer, s2011 integer, s2012 integer,\
#                s2013 integer, s2014 integer, s2015 integer,s2016 integer, average real)'.format(p=pos))
#
#
#cols = pdb.getTableColumnNames(table_name)
#for i in range(len(total[0])):
#    pdb.executeSQL('insert into {tn}({c0}, {c1}, {c2}, {c3}, {c4}, {c5}, {c6}, {c7}) \
#                    VALUES({v0}, {v1}, {v2}, {v3}, {v4}, {v5}, {v6}, {v7})'.\
#                    format(c0=cols[0][1], c1=cols[1][1], c2=cols[2][1], c3=cols[3][1],\
#                           c4=cols[4][1], c5=cols[5][1], c6=cols[6][1], c7=cols[7][1],
#                           v0=total[0][i], v1=total[1][i], v2=total[2][i], v3=total[3][i],\
#                           v4=total[4][i], v5=total[5][i], v6=total[6][i], v7=avg[i],tn=table_name))
#
#pdb.closeDatabase()



