import json
from func import *
from displayStats import *

## For my personal history:
## 2014 - 455893
## 2015 - 898971
## 2016 - 247388
## 2017 - 470610

## https://developer.yahoo.com/yql/console/
## http://jsonviewer.stack.hu/
## https://jsonformatter.curiousconcept.com/

## This is the path to your Yahoo API consumer and secret key
filePath        = '/Users/tbrady/drive/sw/oauth2.json'
oauthToken      = beginOauth2Session(filePath)

season          = 2017
league_id       = 470610
team_id         = 1
week            = 1
roster_size     = 15


leagueSettings  = getLeagueSettings(season, league_id, oauthToken)

#roster          = getWeeklyRoster(season, league_id, team_id, week, roster_size, oauthToken)

matchups         = getWeeklyMatchup(season, league_id, team_id, week, leagueSettings.About.num_teams, oauthToken)

printCleanMatchups(matchups, leagueSettings.About.num_teams)

#print(json.dumps(tmp, indent=2))





#seeAbout       = 1
#seeDates       = 1
#seeScoring     = 1
#
#printCleanSettings(leagueSettings,seeAbout,seeDates,seeScoring)

#printCleanRoster(roster, roster_size)


## still need to figure out week 13 game_id!!
#for i in range(273,331):
#    league_id   = 470610
#    team_id     = 1
#    
#    url     = 'https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys='  \
#                    + str(i) +'.l.' + str(league_id) + '.t.' + str(team_id) + \
#                    '/roster;week=1?format=json'                        
#    jsondata = jsonQuery(url, oauthToken)
#    print (jsondata)
#    print (i)
#    time.sleep(1)
