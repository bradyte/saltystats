#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:00:19 2017

@author: tbrady
"""

import csv

path    = '/Users/tbrady/Documents/GitHub/saltystats/pullFromYahoo/db/'
file    = 'schedule.csv'

with open(path+file, 'r') as csvfile:
    filereader = csv.reader(csvfile)
    schedule = list(filereader)
    
path    += 'clean/'

file    = 'qbpids.csv'
with open(path+file, 'r') as csvfile:
    filereader = csv.reader(csvfile)
    qb = list(filereader)
    
file    = 'rbpids.csv'
with open(path+file, 'r') as csvfile:
    filereader = csv.reader(csvfile)
    rb = list(filereader)
    
file    = 'wrpids.csv'
with open(path+file, 'r') as csvfile:
    filereader = csv.reader(csvfile)
    wr = list(filereader)
    
file    = 'tepids.csv'
with open(path+file, 'r') as csvfile:
    filereader = csv.reader(csvfile)
    te = list(filereader)
    
file    = 'kipids.csv'
with open(path+file, 'r') as csvfile:
    filereader = csv.reader(csvfile)
    ki = list(filereader)
    
file    = 'dstpids.csv'
with open(path+file, 'r') as csvfile:
    filereader = csv.reader(csvfile)
    dst = list(filereader)