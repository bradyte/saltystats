#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:45:05 2017

@author: tbrady
"""

import numpy as np
import settings as ls
import matplotlib.pyplot as plt
import playerDatabase as pdb


def getDefensiveVar(pos, opp_abbr, week):
    table_name = 'def_s2017w' + str(week)
    index_column = pos + 'Pts'
    match_column = 'Team'

#    teams = pdb.executeSQL('SELECT Team FROM {tn}'.format(
#            tn = table_name, ic = index_column))
    pts = pdb.executeSQL('SELECT {ic} FROM {tn} where {mc} = "{mv}"'.format(
            tn = table_name, ic = index_column, mc = match_column, mv = opp_abbr))
    pts = list(map(float, pts))

    return pts


def getCurrentOpponentPerformance(player_id, pos):
    team_id = getTeamIDFromPlayer(player_id, ls.week-1)
    opp_id = getOpponentIDFromTeamID(team_id, ls.week)

    if not opp_id.isnumeric() and opp_id != 'BYE':
            opp_id = int(opp_id[2:])

    opp_abbr = getOppAbbrFromOpponentID(opp_id, ls.week-1)

    tmpPts = []
    for i in range(1,ls.week-1):
        tmp = getDefensiveVar(pos,opp_abbr, i)
        if len(tmp) == 1:
            tmpPts.append(tmp[0])
    tmp = [tmpPts, np.mean(tmpPts), np.std(tmpPts)]
    return tmp[1]




def getPlayerAgainstDefensePerformance(player_id, pos):
    team_id = getTeamIDFromPlayer(player_id, ls.week-1)
    a_prev = [0, 0] # week 0, week 1 doesnt matter for predictions of the current defense

    for week in range(2,ls.week):
        opp_id = getOpponentIDFromTeamID(team_id, week)

        if not opp_id.isnumeric() and opp_id != 'BYE':
                opp_id = opp_id[2:]

        if opp_id != 'BYE':
            tmpList = []
            for j in range(1,ls.week):
                opp_abbr = getOppAbbrFromOpponentID(opp_id, j)
                dv = getDefensiveVar(pos, opp_abbr, j)
                if dv != []:
                    tmpList.append(dv[0])
            tmpList = np.mean(tmpList)
            a_prev.append(tmpList)

    return a_prev





def getTeamIDFromPlayer(player_id, week):
    table_name = 'stats_s' + str(ls.season) + 'w' + str(week)
    index_column = 'team_id'
    match_column = 'player_id'
    team_id = pdb.executeSQL('SELECT {ic} FROM {tn} WHERE {mc} = "{mv}"'.format(
            tn = table_name,
            ic = index_column,
            mc = match_column,
            mv = player_id))[0]
    return team_id

def getOpponentIDFromTeamID(team_id, week):
    table_name = 'schedule_s2017'
    index_column = 'w' + str(week)
    match_column = 'team_id'
    opp_id = pdb.executeSQL('SELECT {ic} FROM {tn}  WHERE {mc} = "{mv}"'.format(
            tn = table_name,
            ic = index_column,
            mc = match_column,
            mv = team_id))[0]
    return opp_id

def getOppAbbrFromOpponentID(opp_id, week):
    table_name = 'stats_s' + str(ls.season) + 'w' + str(week)
    index_column = 'team_abbr'
    match_column = 'team_id'
    opp_abbr = pdb.executeSQL('SELECT {ic} FROM {tn} WHERE {mc} = {mv}'.format(
            tn = table_name,
            ic = index_column,
            mc = match_column,
            mv = opp_id))[0]
    return opp_abbr






