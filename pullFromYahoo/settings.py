#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:48:29 2017

@author: tbrady
"""
import yahooQuery as yq
import cleaning

###############################################################################
## getSeasonGameKey
## This is the key that identifies the fantasy season and fantasy sport
## Made by Yahoo but I had to brute force to get most of these numbers
##
############################################################################### 
def getSeasonGameKey():
    ids = [ 57,  49,  79, 101, 124, 153, 175, 199, 222, \
           242, 257, 273, 314, 331, 348, 359, 371]
    return ids[season - 2001]

 ###############################################################################
## getLeagueSettings
## Similar to the getWeeklyRoster function, I am just picking through the messy
## JSON structure and looking for the only data relevant to me
##
############################################################################### 
def getLeagueSettings():   
    url         = yq.baseURI + 'leagues;league_keys=' \
                + str(game_key) + '.l.' + str(league_id) + '/settings?format=json'
                
    jsondata = yq.jsonQuery(url) 
    
    class LeagueSettings(object):
        class About(object):
            def __init__(self, name=None, num_teams=None, game_code=None,   \
                         url=None, roster_positions=None, rosterSize=None):
                self.name                   = name
                self.num_teams              = num_teams
                self.game_code              = game_code
                self.url                    = url
                self.roster_positions       = roster_positions
                self.rosterSize             = rosterSize
        class Dates(object):
            def __init__(self, season=None, start_week=None, start_date=None,\
                         end_week=None, end_date=None, current_week=None):
                self.season                 = season
                self.start_week             = start_week
                self.start_date             = start_date
                self.end_week               = end_week
                self.end_date               = end_date
                self.current_week           = current_week
        class Scoring(object):
            def __init__(self, uses_fractional_points=None,  \
                         uses_negative_points=None):
                self.uses_fractional_points = uses_fractional_points
                self.uses_negative_points   = uses_negative_points
     
    leagueSettings = LeagueSettings()
    statInfo = []
    ld0 = jsondata['fantasy_content']['leagues']['0']['league'][0]
    ld1 = jsondata['fantasy_content']['leagues']['0']['league'][1]['settings']
    
    ##about
    leagueSettings.About.name           = ld0['name']
    leagueSettings.About.num_teams      = ld0['num_teams']
    leagueSettings.About.game_code      = ld0['game_code']
    leagueSettings.About.url            = ld0['url']
    [pos, sz] = cleaning.cleanPositions(ld1[0]['roster_positions'])
    leagueSettings.About.roster_positions = pos
    leagueSettings.About.roster_size    = sz

    ##dates
    leagueSettings.Dates.start_week     = ld0['start_week']
    leagueSettings.Dates.end_week       = ld0['end_week']
    leagueSettings.Dates.current_week   = ld0['current_week']
    leagueSettings.Dates.season         = ld0['season']
    leagueSettings.Dates.start_date     = ld0['start_date']
    leagueSettings.Dates.end_date       = ld0['end_date']
    
    ##scoring
    leagueSettings.Scoring.uses_fractional_points   = yq.searchJSONObject(ld1, 'uses_fractional_points')
    leagueSettings.Scoring.uses_negative_points     = yq.searchJSONObject(ld1, 'uses_negative_points')

    statInfo  = cleaning.cleanStats(ld1[0]['stat_categories']['stats'], ld1[0]['stat_modifiers']['stats'])
    
    return [leagueSettings, statInfo]

    


## For my personal history:
## 2014 - 455893
## 2015 - 898971
## 2016 - 247388
## 2017 - 470610
season          = 2017
league_id       = 470610  
game_key        = getSeasonGameKey()
[leagueSettings, statInfo] = getLeagueSettings()
temp = getLeagueSettings()


#for i in range(len(statInfo[0])):
#    print('{}|{}|{}'.format(i,statInfo[1][i],str(statInfo[0][i])))

roster_size     = leagueSettings.About.roster_size

week            = leagueSettings.Dates.current_week
team_id         = 1

statName       = \
[   'active',       # 0
    'pass_att',     # 1
    'pass_comp',
    'pass_miss',
    'pass_yds',
    'pass_td',
    'pass_int',
    'Field7',
    'rush_att',
    'rush_yds',
    'rush_td',
    'rec',
    'rec_yds',
    'rec_td',
    'Field14',
    'ret_td',
    'two_pt',
    'fum',
    'fum_lost',
    'fg_0_19',
    'fg_20_29',
    'fg_30_39',
    'fg_40_49',
    'fg_50_plus',
    'Field24',
    'Field25',
    'Field26',
    'Field27',
    'Field28',
    'pat_made',
    'pat_miss',
    'def_pa',
    'def_sack',
    'def_int',
    'def_fum_rec',
    'def_td',
    'def_sfty',
    'def_blk_kick',
    'idp_s_tkl',
    'idp_a_tkl',
    'idp_sack',
    'Field41',
    'Field42',
    'Field43',
    'Field44',
    'Field45',
    'idp_pass_def',
    'Field47',
    'def_ret_yds',
    'ko_pr_ret_td',
    'def_pa_0',
    'def_pa_1_6',
    'def_pa_7_13',
    'def_pa_14_20',
    'def_pa_21_27',
    'def_pa_28_34',
    'def_pa_35_plus',
    'off_fum_ret_td',
    'Field58',
    'Field59',
    'Field60',
    'Field61',
    'Field62',
    'Field63',
    'Field64',
    'def_tkl_fl',
    'Field66',
    'def_4d_stop',
    'Field68',
    'Field69',
    'Field70',
    'Field71',
    'Field72',
    'Field73',
    'Field74',
    'Field75',
    'Field76',
    'Field77',
    'targets',
    'Field79',
    'Field80',
    'Field81',
    'xpr',
    'player_id',        # 83
    'team_id',          # 84
    'position',         # 85
    'name',             # 86
    'team_abbr',        # 87
    'fpts']             # 88




























