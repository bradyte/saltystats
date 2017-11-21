from cleaning import *

import league_settings as ls







###############################################################################
## getWeeklyRoster
## This returns a roster class that has the roster based on week and 
## team_id
##
###############################################################################  
#def getWeeklyRoster(season, league_id, team_id, week, roster_size, oauthToken):
#    url         = 'https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys=' \
#                + str(ls.game_key) +'.l.' + str(ls.league_id) + '.t.' + str(team_id)  \
#                + '/roster;week=' + str(ls.week) + '/players/stats;type=week;week='\
#                + str(ls.week) + '?format=json'
#                        
#    jsondata = ls.jsonQuery(url)
#    
#    roster = [];
#    
#    class Player(object):
#        def __init__(self, player_id, name_full, editorial_team_abbr, display_position, \
#                     selected_position, player_points, player_stats=None):
#            self.player_id              = player_id
#            self.name_full              = name_full
#            self.editorial_team_abbr    = editorial_team_abbr
#            self.display_position       = display_position
#            self.selected_position      = selected_position
#            self.player_points          = player_points
#            self.player_stats           = player_stats  # raw stats if we ever want to do more analysis on the stats
#           
#    for i in range(0,roster_size):
#        playerData          = YahooIsGarbage(jsondata, i)
#        player_id           = [d['player_id']               for d in playerData if 'player_id'              in d][0]
#        name_full           = [d['name']['full']            for d in playerData if 'name'                   in d][0]
#        editorial_team_abbr = [d['editorial_team_abbr']     for d in playerData if 'editorial_team_abbr'    in d][0]
#        display_position    = [d['display_position']        for d in playerData if 'display_position'       in d][0]
#        selected_position   = [d['position']                for d in playerData if 'position'               in d][0]
#        player_points       = [d['player_points']['total']  for d in playerData if 'player_points'          in d][0]
#
#        roster.append(Player(player_id, name_full, editorial_team_abbr, display_position, selected_position, float(player_points)))
#
#    return roster;

###############################################################################
## getLeagueSettings
## Similar to the getWeeklyRoster function, I am just picking through the messy
## JSON structure and looking for the only data relevant to me
##
############################################################################### 
def getLeagueSettings():   
    url         = 'https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=' \
                + str(ls.game_key) + '.l.' + str(ls.league_id) + '/settings?format=json'
                
    leaguedata = ls.jsonQuery(url)
    
    class LeagueSettings(object):
        class About(object):
            def __init__(self, name=None, num_teams=None, game_code=None, url=None, roster_positions=None, rosterSize=None):
                self.name                   = name
                self.num_teams              = num_teams
                self.game_code              = game_code
                self.url                    = url
                self.roster_positions       = roster_positions
                self.rosterSize             = rosterSize
        class Dates(object):
            def __init__(self, season=None, start_week=None, start_date=None, end_week=None, end_date=None, current_week=None):
                self.season                 = season
                self.start_week             = start_week
                self.start_date             = start_date
                self.end_week               = end_week
                self.end_date               = end_date
                self.current_week           = current_week
        class Scoring(object):
            def __init__(self, statInfo=None, uses_fractional_points=None, uses_negative_points=None):
                self.statInfo               = statInfo
                self.uses_fractional_points = uses_fractional_points
                self.uses_negative_points   = uses_negative_points
     
    leagueSettings = LeagueSettings()
        
    ##about
    leagueSettings.About.name                       \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['name']
    leagueSettings.About.num_teams                  \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['num_teams']
    leagueSettings.About.game_code                  \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['game_code']
    leagueSettings.About.url                        \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['url']
    leagueSettings.About.roster_positions           \
        = cleanPositions(leaguedata['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['roster_positions'])
    leagueSettings.About.rosterSize = 0
    for i in range(0,len(leagueSettings.About.roster_positions )):
        leagueSettings.About.rosterSize = leagueSettings.About.rosterSize + leagueSettings.About.roster_positions[i].count
    
    
    ##dates

    leagueSettings.Dates.start_week                 \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['start_week']
    leagueSettings.Dates.end_week                   \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['end_week']
    leagueSettings.Dates.current_week               \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['current_week']
    leagueSettings.Dates.season                     \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['season']
    leagueSettings.Dates.start_date                 \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['start_date']
    leagueSettings.Dates.end_date                   \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['end_date']
    
    ##scoring
    leagueSettings.Scoring.uses_fractional_points   \
        = leaguedata['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['uses_fractional_points']
    leagueSettings.Scoring.uses_negative_points     \
        = leaguedata['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['uses_negative_points']
    leagueSettings.Scoring.statInfo                 \
        = cleanStats(leaguedata['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['stat_modifiers']['stats'],\
                     leaguedata['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['stat_categories']['stats'])

    return leagueSettings;

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
def getPlayerStats(player_id, statValues):
    url         = 'https://fantasysports.yahooapis.com/fantasy/v2/player/' \
                + str(ls.game_key) + '.p.' + str(player_id) \
                + '/stats;type=week;week=' + str(ls.week) +'?format=json'
                
    jsondata = ls.jsonQuery(url)
    
    byeWeek  = int(jsondata['fantasy_content']['player'][0][7]['bye_weeks']['week'])
    
    if ls.week == byeWeek:
        return 'BYE'
    else:
        tmpStats = jsondata['fantasy_content']['player'][1]['player_stats']['stats']
        fpts = 0
        for i in range(0,len(tmpStats)):
            
            stat_id = int(tmpStats[i]['stat']['stat_id'])
            value   = float(tmpStats[i]['stat']['value'])
            fpts = round(fpts + value * statValues[stat_id], 2) 
        
        return fpts;

    
    
def doesPlayerExist(player_id):
    url         = 'https://fantasysports.yahooapis.com/fantasy/v2/player/'  \
                + str(ls.game_key) + '.p.' + str(player_id)    \
                + '/stats;type=week;week=' + str(ls.week) + '?format=json'
                
    jsondata    = ls.jsonQuery(url)
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
#        return jsondata

    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    