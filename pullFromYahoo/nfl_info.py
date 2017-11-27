#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:00:19 2017

@author: tbrady
"""

import csv
import settings as ls

path    = 'db/'
sch_file    = 'schedule/schedule.csv'

with open(path+sch_file, 'r') as csvfile:
    filereader = csv.reader(csvfile)
    schedule = list(filereader)
    
#ply_file    = 'stats/playerDB.csv'
#
#with open(path+ply_file, 'r') as csvfile:
#    filereader = csv.reader(csvfile)
#    playerDB = list(filereader)
#    
