import json
import time
from func import *

# For my personal history:
# 2014 - 455893
# 2015 - 898971
# 2016 - 247388
# 2017 - 470610

# This is the path to your Yahoo API consumer and secret key
filePath        = '/Users/tbrady/drive/sw/oauth2.json'
oauthToken      = beginOauth2Session(filePath)

season          = 2017
league_id       = 470610
team_id         = 1
week            = 1



leagueSettings  = getLeagueSettings(season, league_id, oauthToken)



roster          = getWeeklyRoster(season, league_id, team_id, week, oauthToken)
#printCleanRoster(roster)



lenModifiers = len(leagueSettings.Scoring.stat_modifiers)
maxID = 0

for i in range(0,lenModifiers):
    tmp = leagueSettings.Scoring.stat_modifiers[i]['stat']['stat_id']
    if int(tmp) > maxID:
        maxID = tmp  
    


class StatInfo(object):
    def __init__(self, display_name=None, value=None):
        self.display_name   = display_name
        self.value          = value

statInfo = StatInfo()

## initialize arrays to use Yahoo's stupid stat_id as the index parameter
statInfo.display_name   = [None] * maxID
statInfo.value          =    [0] * maxID


                

#for i in range(0,numStats):
#    leagueSettings.Scoring.stat_modifiers[i] = leagueSettings.Scoring.stat_modifiers[i]['stat']['stat_id']
#    leagueSettings.Scoring.stat_categories[i] = leagueSettings.Scoring.stat_categories[i]['stat']['stat_id']
#    
#    print(leagueSettings.Scoring.stat_modifiers[i]," ",leagueSettings.Scoring.stat_categories[i])



#json.dumps(json.loads(str(tmp,'utf-8')), indent=2)











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
