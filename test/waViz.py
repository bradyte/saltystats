#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:19:20 2017

@author: tbrady
"""
from datetime import datetime
import time
import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
from matplotlib.dates import epoch2num, date2num

f = open('whatsappHistory.txt','r')
x = f.readlines()
times = [i.split('-')[0] for i in x]
msgs = [i.split('-') for i in x]

t0 = datetime(2015,8,24,11,28) #8/24/15, 11:28 AM
t0 = time.mktime(t0.timetuple())

tm_year = []
tm_mon = []
tm_mday = []
tm_hour = []
tm_min = []
tm = []
#for i in range(len(times)):
for i in range(20000,30000):
    if times[i]:
        if times[i][0].isnumeric() and len(times[i]) > 3:
            try:
                t = []
                t = times[i]
                tmp = re.split(',|:|/| ',t)

                tm_year = int('20'+tmp[2])
                tm_mon = int(tmp[0])
                tm_mday = int(tmp[1])

                if tmp[6] == 'PM'  and tmp[4] != '12':
                    tm_hour = int(tmp[4]) + 12

                else:
                    tm_hour = int(tmp[4])
                tm_min = int(tmp[5])


                epoch = datetime(tm_year, tm_mon, tm_mday, tm_hour, tm_min)
                tm.append(time.mktime(epoch.timetuple()))
            except (IndexError, ValueError, NameError) as e:
                pass


years = YearLocator()   # every year
months = MonthLocator()  # every month
yearsFmt = DateFormatter('%Y')

(hist, bin_edges) = np.histogram(tm, 100)
fig, ax = plt.subplots()
width = bin_edges[1] - bin_edges[0]
years = YearLocator()
ax.bar(bin_edges[:-1], hist / width, width=width)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

datemin = np.datetime64(r.date[0], 'Y')
datemax = np.datetime64(r.date[-1], 'Y') + np.timedelta64(1, 'Y')
ax.set_xlim(datemin, datemax)

ax.set_xlim(bin_edges[0], bin_edges[100])
ax.format_xdata = DateFormatter('%Y-%m-%d')
ax.grid(True)
fig.autofmt_xdate()
plt.show()




