import settings as ls
import func as f
import matplotlib.pyplot as plt

import pprint
import time



## https://developer.yahoo.com/yql/console/
## http://jsonviewer.stack.hu/
## https://jsonformatter.curiousconcept.com/


teamInfo    = f.getTeamManagerInfo(ls.team_id)
teamRoster  = f.getTeamWeeklyRoster(ls.team_id)

data = []
for i in range(len(teamRoster)):
    data.append(f.getPlayerInfoDB(teamRoster[i]))




[leagueSettings, statInfo] = ls.getLeagueSettings()









#29399
#9317
#30199 hunt downward trend
#6762 fitzgerald inconsistent
#29236 wentz very good
#28461 coleman consistent


#fpts        = []
#fptsArr     = []
#fptsPlotArr = []
#fptsMean    = 0.0
#fptsStdev   = 0.0
#fptsCV      = 0.0
#fptsROC     = 0.0
#fptsPDF     = 0.0
#fptsSE      = 0.0 # standard error of mean
#fptsVar     = 0.0
#confInt     = 1.96  # z* of 95%
#confLimits  = 0.0
#k = 0
#ksum = 0
#player_id = 100001
#for i in range(player_id,player_id+34):
#    if (i != 100031) and (i != 100032):
#        url = 'https://fantasysports.yahooapis.com/fantasy/v2/player/'  \
#            + str(getSeasonGameKey(season)) + '.p.' + str(i)    \
#            + '/stats;type=week;week=' + str(week) + '?format=json'
#        jsondata = jsonQuery(url, oauthToken)
#        jsondataText = jsondata['fantasy_content']['player'][0][2]['name']['full']
#        jsondataStats = int(jsondata['fantasy_content']['player'][1]['player_stats']['stats'][19]['stat']['value'])
#        if jsondataStats > 0:
#            k += 1
##        pprint.pprint(jsondataStats)
#        ksum += jsondataStats
##    time.sleep(2)
#print(ksum/k)
    

#title       = getPlayerName(season, player_id, week, oauthToken)
#print('Week:     Fpts      Average   Stdev     CV        ROC       Margin+/-') 
#for i in range(1, int(leagueSettings.Dates.current_week)):
#    fpts.append(getPlayerStats(season, player_id, i, leagueSettings.Scoring.statInfo.value, oauthToken))
#    if fpts[i-1] != 'BYE':
#        fptsArr.append(fpts[i-1])
#        fptsMean    = round(numpy.mean(fptsArr), 2)
#        fptsStdev   = round(numpy.std(fptsArr), 2)
#        if i == 1:
#            fptsCV      = 0.0
#            fptsROC     = 0.0
#            fptsEXP     = 0.0
#        else:
#            fptsCV      = round(fptsStdev/fptsMean, 2)
#            fptsROC     = round(fpts[i-1]/fptsMean, 2)
#            fptsSE      = round(confInt*fptsStdev/numpy.sqrt(i),2)
##            fptsVar     = round(fptsROC/fptsStdev,3)
#        plt.subplot(211)    
#        plt.scatter(i, fpts[i-1])
#        plt.xlabel('Week')
#        plt.title(title)
#        plt.axis([0, 17, 0, 40]) 
#        plt.grid(True)
#        
#        plt.subplot(212) 
#        plt.scatter(i, fptsVar)
#        plt.xlabel('Week')
#        plt.title('CV')
#        plt.axis([0, 17, 0, 0.6]) 
#        plt.grid(True)
#    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(\
#          i,fpts[i-1], fptsMean, fptsStdev, fptsCV, fptsROC, fptsSE))
#
# 
#
#plt.subplots_adjust(wspace=0.8, hspace=0.8)
#plt.show()


#needed to initialize class
#leagueSettings.About.num_teams
#leagueSettings.Dates.start_week
#leagueSettings.Dates.end_week
#fpts = getPlayerStats(season, 9317, 1, leagueSettings.Scoring.statInfo.value, oauthToken)



#getWeeklyOutcome
#week = [None] * (int(leagueSettings.Dates.end_week) + 1)
#team = [0] * (int(leagueSettings.About.num_teams) + 1)

##roster = []
#roster = \
#{
#    'roster': [
#        {
#           'position': 'QB',
#           'player_id': 8780
#        },
#        {
#            'position': 'WR',
#            'player_id': 9600
#        }
#    ]
#}
#
##
#week = {}
#week = []
#week.append({})
#week.append({'team': [{}] })
#week[1]['team'].append(roster)
#
##week.append({
##    'team': [
##        {},
##        {
##        'roster': [
##            {
##                'position': 'WR',
##                'player_id': 9600
##            }    
##        ],
##        'total' : 100,
##        'opponent': 2,
##        'oppTotal': 120
##        }
##    ]  
##})

#roster          = getWeeklyRoster(season, league_id, team_id, week, roster_size, oauthToken)
#matchups         = getWeeklyMatchup(season, league_id, team_id, week, leagueSettings.About.num_teams, oauthToken)
#printCleanMatchups(matchups, leagueSettings.About.num_teams)
#print(json.dumps(tmp, indent=2))


#seeAbout       = 1
#seeDates       = 1
#seeScoring     = 1
###
#printCleanSettings(leagueSettings,seeAbout,seeDates,seeScoring)
#
#printCleanRoster(roster, roster_size)
