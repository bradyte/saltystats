import cleaning
import settings as ls
import nfl_info as nfl
import csv

###############################################################################
## getTeamManagerInfo
## This returns a manager class that has the roster based on team_id
## 
##
###############################################################################  
def getTeamManagerInfo(team_id):
    url     = 'https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys='     \
            + str(ls.game_key) +'.l.' + str(ls.league_id) + '.t.' + str(team_id)    \
            + '/roster;week=' + str(ls.week) + '/players/stats;type=week;week='     \
            + str(ls.week) + '?format=json'
    
    class ManagerInfo(object):
        def __init__(self, team_key=None, team_id=None, team_name=None,     \
                     waiver_priority=None, faab_balance=None,               \
                     number_of_moves=None, nickname=None):
            self.team_key           = team_key
            self.team_id            = team_id
            self.team_name          = team_name
            self.waiver_priority    = waiver_priority
            self.faab_balance       = faab_balance
            self.number_of_moves    = number_of_moves
            self.nickname           = nickname  
    
    jsondata = jsonQuery(url)        
    tmp0 = jsondata['fantasy_content']['teams']['0']['team'][0]

    
    mi = ManagerInfo()
    
    mi.team_key         = searchJSONObject(tmp0, 'team_key')
    mi.team_id          = searchJSONObject(tmp0, 'team_id')  
    mi.team_name        = searchJSONObject(tmp0, 'team_name')
    mi.waiver_priority  = searchJSONObject(tmp0, 'waiver_priority')  
    mi.faab_balance     = searchJSONObject(tmp0, 'faab_balance')   
    mi.number_of_moves  = searchJSONObject(tmp0, 'number_of_moves')
    mi.nickname         = searchJSONObject(tmp0, 'nickname')  
  
    return mi;



###############################################################################
## getWeeklyRoster
## This returns a roster class that has the roster based on week and 
## team_id
##
###############################################################################  
def getTeamWeeklyRoster(team_id):
    url     = 'https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys='     \
            + str(ls.game_key) +'.l.' + str(ls.league_id) + '.t.' + str(team_id)    \
            + '/roster;week=' + str(ls.week) + '/players/stats;type=week;week='     \
            + str(ls.week) + '?format=json'
            
    jsondata = fy.jsonQuery(url)        
    data = []
    
    for i in range(ls.roster_size):
        playerData          = cleaning.cleanPlayerData(jsondata, i)
        player_id           = fy.searchJSONObject(playerData, 'player_id')
        selected_position   = fy.searchJSONObject(playerData, 'selected_position')
        display_position    = fy.searchJSONObject(playerData, 'display_position')
        data.append([int(player_id),str(display_position), str(selected_position)])
      
    roster = []
    for i in range(len(data)):
        roster.append(getPlayerInfoDB(data[i]))
    return roster





###############################################################################
## getWeeklyMatchup
## 
## 
##
############################################################################### 
#def getWeeklyMatchup(season, league_id, team_id, week, num_teams, oauthToken):
#    game_key    = getSeasonGameKey(season)
#    url         = 'https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=' \
#                + str(game_key) + '.l.' + str(league_id)  \
#                + '/scoreboard;week=' + str(week) + '?format=json'
#                        
#    jsondata = jsonQuery(url, oauthToken)
#    
#    class Matchups(object):
#        def __init__(self, winner_team_key=None, team0_team_key=None, team0_total=None, team1_team_key=None, team1_total=None):
#            self.winner_team_key = winner_team_key
#            self.team0_team_key  = team0_team_key
#            self.team0_total     = team0_total
#            self.team1_team_key  = team1_team_key
#            self.team1_total     = team1_total
#    
#    matchup = []
#    for i in range(0,int(num_teams/2)):
#        winner_team_key = jsondata['fantasy_content']['leagues']['0']['league'][1]['scoreboard']['0']['matchups'][str(i)]['matchup']['winner_team_key']
#        team0_team_key  = jsondata['fantasy_content']['leagues']['0']['league'][1]['scoreboard']['0']['matchups'][str(i)]['matchup']['0']['teams']['0']['team'][0][0]['team_key']
#        team0_total     = jsondata['fantasy_content']['leagues']['0']['league'][1]['scoreboard']['0']['matchups'][str(i)]['matchup']['0']['teams']['0']['team'][1]['team_points']['total']
#        team1_team_key  = jsondata['fantasy_content']['leagues']['0']['league'][1]['scoreboard']['0']['matchups'][str(i)]['matchup']['0']['teams']['1']['team'][0][0]['team_key']
#        team1_total     = jsondata['fantasy_content']['leagues']['0']['league'][1]['scoreboard']['0']['matchups'][str(i)]['matchup']['0']['teams']['1']['team'][1]['team_points']['total']
#    
#        matchup.append(Matchups(winner_team_key, team0_team_key, float(team0_total), team1_team_key, float(team1_total)))
#
#    return matchup;

###############################################################################
## getPlayerStats
## 
## 
##
############################################################################### 
def getPlayerStats(player_id):
    url         = 'https://fantasysports.yahooapis.com/fantasy/v2/player/' \
                + str(ls.game_key) + '.p.' + str(player_id) \
                + '/stats;type=week;week=' + str(ls.week) +'?format=json'
                
    jsondata = fy.jsonQuery(url)
    
    byeWeek     = fy.searchJSONObject(jsondata['fantasy_content']['player'][0], 'bye_weeks')
    byeWeek     = int(byeWeek['week'])
    
    if ls.week == byeWeek:
        return 'BYE'
    else:
        tmpStats = jsondata['fantasy_content']['player'][1]['player_stats']['stats']
        fpts = 0
        for i in range(0,len(tmpStats)):
            
            stat_id = int(tmpStats[i]['stat']['stat_id'])
            value   = float(tmpStats[i]['stat']['value'])
            fpts = round(fpts + value * ls.statInfo[1][stat_id], 2) 
        
        return fpts;




    
###############################################################################
## getPlayerInfoQuery
## 
## 
##
###############################################################################     
def getPlayerInfoQuery(player_id):

    url         = 'https://fantasysports.yahooapis.com/fantasy/v2/player/'  \
                + str(ls.game_key) + '.p.' + str(player_id)                 \
                + '/stats;type=week;week=' + str(ls.week) + '?format=json'
                
    jsondata    = fy.jsonQuery(url)
    team_id     = 0
    name        = None
    position    = None
    team_abbr   = None
    
    if 'error' in jsondata:
        return [player_id, team_id, position, name, team_abbr]
    else:
        jsondata = jsondata['fantasy_content']['player']
        name = str(jsondata[0][2]['name']['full'])
        position = None
        for d in jsondata[0]:
            if 'display_position' in d:
                position = d['display_position']
            if 'editorial_team_abbr' in d:
                team_abbr = d['editorial_team_abbr']
            if 'editorial_team_key' in d:
                tmp = str(d['editorial_team_key'])
                tmp = tmp.split('.')
                team_id = int(tmp[2])
        return [player_id, team_id, str(position), str(name), str(team_abbr)]
    
###############################################################################
## getPlayerInfoDB
## 
## 
##
###############################################################################     
def getPlayerInfoDB(info):
    team_id     = 0
    name        = None
    team_abbr   = None
    lst         = None
    
    player_id   = info[0]
    position    = info[1]
    selected_position = info[2]
    
    if position == 'QB':
        lst = nfl.qb
    elif position == 'WR':
        lst = nfl.wr
    elif position == 'RB':
        lst = nfl.rb
    elif position == 'TE':
        lst = nfl.te
    elif position == 'K':
        lst = nfl.ki
    elif position == 'DEF':
        lst = nfl.dst
        
    if lst != None:
        for row in range(len(lst)):
            if player_id == int(lst[row][0]):
                return [player_id, int(lst[row][1]), str(selected_position), str(lst[row][3]), str(lst[row][4])]
    else:
        return [player_id, int(team_id), str(selected_position), str(name), str(team_abbr)]
            
        
            
            
            
            
   
    
    
###############################################################################
## getLeagueTransactionQuery
## 
## 
##
############################################################################### 
def getLeagueTransactionQuery():
    url         = 'https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=' \
                + str(ls.game_key) + '.l.' + str(ls.league_id) \
                + '/transactions?format=json'
    jsondata    = fy.jsonQuery(url)
    transactions  = jsondata['fantasy_content']['leagues']['0']['league'][1]['transactions']
    

    
###############################################################################
## getPlayerStats
## 
## 
##
############################################################################### 
def updatePlayerStatsQuery(player_id):
    url         = 'https://fantasysports.yahooapis.com/fantasy/v2/player/' \
                + str(ls.game_key) + '.p.' + str(player_id) \
                + '/stats;type=week;week=' + str(ls.week) +'?format=json'
                
    jsondata    = fy.jsonQuery(url)
    byeWeek     = fy.searchJSONObject(jsondata['fantasy_content']['player'][0], 'bye_weeks')
    tmpStats    = jsondata['fantasy_content']['player'][1]['player_stats']['stats']
    byeWeek     = int(byeWeek['week'])
    bsa         = ls.blankStatsArray

    if ls.week == byeWeek:
        bsa[0]  = 'BYE'
    else:
        for i in range(0,len(tmpStats)):
            stat_id         = int(tmpStats[i]['stat']['stat_id'])
            bsa[stat_id]    = float(tmpStats[i]['stat']['value'])
     
    idx = 0
    tmpList = []
    tmpCSV = []
    with open('db/outfile.csv','r') as infile:
        reader = csv.reader(infile)
        tmpCSV.extend(reader)
        
    with open('db/outfile.csv','r') as infile:
        reader = csv.reader(infile)        
        while(idx != player_id):
            row = next(reader)
            idx = int(float(row[0]))            
            tmpList = list(row)

#    print('here')
    tmpList.extend(bsa)
    ovr = {idx:tmpList}
    with open('db/outfile.csv','w') as outfile:
        writer = csv.writer(outfile)
        for line, row in enumerate(tmpCSV):
            data = ovr.get(line,row)
            writer.writerow(data)



#        return tmpList
    
    
#    return bsa  


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    