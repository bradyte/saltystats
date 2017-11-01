import json
import time
from func import *

# This is the path to your Yahoo API consumer and secret key
filePath    = '/Users/tbrady/drive/sw/oauth2.json'
oauthToken  = beginOauth2Session(filePath)

# For my personal history:
# 2014 - 455893
# 2015 - 898971
# 2016 - 247388
# 2017 - 470610


season      = 2017
league_id   = 470610
team_id     = 1
week        = 1

#roster      = getWeeklyRoster(season, league_id, team_id, week, oauthToken)

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

#printCleanRoster(roster)
leagueSettings         = getLeagueSettings(season, league_id, oauthToken)

##about
#name                   = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['name']
#num_teams              = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['num_teams']
#game_code              = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['game_code']
#url                    = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['url']
#roster_positions       = leagueSettings['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['roster_positions']

##dates
#season                 = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['season']
#start_week             = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['start_week']
#start_date             = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['start_date']
#end_week               = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['end_week']
#end_date               = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['end_date']
#current_week           = leagueSettings['fantasy_content']['leagues']['0']['league'][0]['current_week']

##scoring
#stat_categories        = leagueSettings['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['stat_categories']['stats']
#stat_modifiers         = leagueSettings['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['stat_modifiers']['stats']
#uses_fractional_points = leagueSettings['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['uses_fractional_points']
#uses_negative_points   = leagueSettings['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['uses_negative_points']


data = leagueSettings['fantasy_content']['leagues']['0']['league']
print(json.dumps(data, indent=2))


