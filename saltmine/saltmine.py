#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 10:46:49 2018

@author: tombrady
"""

import yahooOauth2
import settings as ls



ls.season = 2017
ls.league_id = 470610  
ls.game_key = ls.getSeasonGameKey(ls.season)

temp = ls.getLeagueSettings(ls.season, ls.league_id, ls.game_key)