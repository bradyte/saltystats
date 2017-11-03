import json  
from yahoo_oauth import OAuth2

###############################################################################
## beginOauth2Session
## input: file path to the oauth.json file
## output: reusable token for queries to the Yahoo API
##
###############################################################################
def beginOauth2Session(filePath):
    
##  For your Oauth2 JSON file, please use the following format
##  {
##      "consumer_key":    "<CONSUMER_KEY>",
##      "consumer_secret": "<CONSUMER_SECRET>",
##  }
    oauthToken = OAuth2(None, None, from_file=filePath)
    if not oauthToken.token_is_valid():
        oauthToken.refresh_access_token()
    return oauthToken;

###############################################################################
## jsonQuery
## input: query url, oauthToken
## output: result from query in raw JSON format
##
###############################################################################  
def jsonQuery(url, oauthToken) :
    
    response = oauthToken.session.get(url)
    jsondata =json.loads(str(response.content,'utf-8'))
#    print(json.dumps(jsondata, indent=2))
    return jsondata;

###############################################################################
## YahooIsGarbage
## Meant to clean up the player data from four seperate lists into one list
##
##
############################################################################### 
def YahooIsGarbage(jsondata, i):
    
    class Struct(object):
        def __init__(self, **entries):
            self.__dict__.update(entries)
    
    playerData0 = jsondata['fantasy_content']['teams']['0']['team'][1]['roster']['0']['players'][str(i)]['player'][0]
    tmp         = jsondata['fantasy_content']['teams']['0']['team'][1]['roster']['0']['players'][str(i)]['player'][1]
    tmp         = Struct(**tmp)
    playerData1 = tmp.selected_position
    playerData2 = jsondata['fantasy_content']['teams']['0']['team'][1]['roster']['0']['players'][str(i)]['player'][2]
    playerData3 = jsondata['fantasy_content']['teams']['0']['team'][1]['roster']['0']['players'][str(i)]['player'][3]

    playerData  = playerData0 + playerData1
    
    playerData.append(dict(playerData2))
    playerData.append(dict(playerData3))
    return playerData;

###############################################################################
## getSeasonGameKey
## This is the key that identifies the fantasy season and fantasy sport
## Made by Yahoo but I had to brute force to get most of these numbers
##
############################################################################### 
def getSeasonGameKey(season):
##   season_ids
##   2001 - 57    2002 - 49    2003 - 79    2004 - 101   2005 - 124
##   2006 - 153   2007 - 175   2008 - 199   2009 - 222   2010 - 242
##   2011 - 257   2012 - 273   2013 - 999   2014 - 331   2015 - 348
##   2016 - 359   2017 - 371
    
    ids = [ 57,  49,  79, 101, 124, \
           153, 175, 199, 222, 242, \
           257, 273, 999, 331, 348, \
           359, 371]
    season_id = ids[season - 2001]
    return season_id;
  
###############################################################################
## getWeeklyRoster
## This returns a roster class that has the roster based on week and 
## team_id
##
###############################################################################  
def getWeeklyRoster(season, league_id, team_id, week, roster_size, oauthToken):
    
    game_key    = getSeasonGameKey(season)
    url     = 'https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys=' \
                + str(game_key) +'.l.' + str(league_id) + '.t.' + str(team_id)  \
                + '/roster;week=' + str(week) + '/players/stats;type=week;week='\
                + str(week) + '?format=json'
                        
    jsondata = jsonQuery(url, oauthToken)
    
    roster = [];
    
    class Player(object):
        def __init__(self, player_id, name_full, editorial_team_abbr, display_position, \
                     selected_position, player_points, player_stats=None):
            self.player_id              = player_id
            self.name_full              = name_full
            self.editorial_team_abbr    = editorial_team_abbr
            self.display_position       = display_position
            self.selected_position      = selected_position
            self.player_points          = player_points
            self.player_stats           = player_stats  # raw stats if we ever want to do more analysis on the stats
           
    for i in range(0,roster_size):
        playerData          = YahooIsGarbage(jsondata, i)
        player_id           = [d['player_id']               for d in playerData if 'player_id'              in d][0]
        name_full           = [d['name']['full']            for d in playerData if 'name'                   in d][0]
        editorial_team_abbr = [d['editorial_team_abbr']     for d in playerData if 'editorial_team_abbr'    in d][0]
        display_position    = [d['display_position']        for d in playerData if 'display_position'       in d][0]
        selected_position   = [d['position']                for d in playerData if 'position'               in d][0]
        player_points       = [d['player_points']['total']  for d in playerData if 'player_points'          in d][0]

        roster.append(Player(player_id, name_full, editorial_team_abbr, display_position, selected_position, float(player_points)))

    return roster;

###############################################################################
## getLeagueSettings
## Similar to the getWeeklyRoster function, I am just picking through the messy
## JSON structure and looking for the only data relevant to me
##
############################################################################### 
def getLeagueSettings(season, league_id, oauthToken):
    
    game_key    = getSeasonGameKey(season)    
    url     = 'https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=' \
                + str(game_key) + '.l.' + str(league_id) + '/settings?format=json'
                
    leaguedata = jsonQuery(url, oauthToken)
    
    class LeagueSettings(object):
        class About(object):
            def __init__(self, name=None, num_teams=None, game_code=None, url=None, roster_positions=None):
                self.name                   = name
                self.num_teams              = num_teams
                self.game_code              = game_code
                self.url                    = url
                self.roster_positions       = roster_positions
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
        = cleanPositions(                           \
          leaguedata['fantasy_content']['leagues']['0']['league'][1]['settings'][0]['roster_positions'])
    
    ##dates
    leagueSettings.Dates.season                     \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['season']
    leagueSettings.Dates.start_week                 \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['start_week']
    leagueSettings.Dates.start_date                 \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['start_date']
    leagueSettings.Dates.end_week                   \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['end_week']
    leagueSettings.Dates.end_date                   \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['end_date']
    leagueSettings.Dates.current_week               \
        = leaguedata['fantasy_content']['leagues']['0']['league'][0]['current_week']
    
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
## cleanStats
## Searches for stat info based on stat_id. Very confusing because the stat_id
## is not the index number so I make a new list indexed by the stat_id
##
############################################################################### 
def cleanStats(mods, cats):

## oddly enough, these aren't always equal
    lenModifiers = len(mods)
    lenCategories = len(cats)
    maxID = 0
    
## get the last stat_id value, we only care about modifiers since those are
## used for scoring. there are stat_categories that have zero use    
    for i in range(0,lenModifiers):
        tmp = mods[i]['stat']['stat_id']
        if int(tmp) > maxID:
            maxID = tmp  
        
    class StatInfo(object):
        def __init__(self, display_name=None, value=None):
            self.display_name   = display_name
            self.value          = value
    
    statInfo = StatInfo()
    
## initialize arrays to use Yahoo's stupid stat_id as the index size
    statInfo.display_name   = [None] * (maxID+1)
    statInfo.value          =    [0] * (maxID+1)
       
## use stat_id from the stat_modifiers to search the stat_categories  
    for i in range(0,lenModifiers):
        statIndex = mods[i]['stat']['stat_id']
        statInfo.value[statIndex] = float(mods[i]['stat']['value'])
## walk through the category list and only get categories that have modifiers
## associated with them        
        j = 0
        while(j < lenCategories):
            tmpCat = cats[j]['stat']['stat_id']
            if tmpCat == statIndex:
               statInfo.display_name[statIndex] = cats[j]['stat']['display_name']
            j += 1

    return statInfo;
                
###############################################################################
## cleanPositions
## break up the two categories to index a lot more easily
## 
##
############################################################################### 
def cleanPositions(pos):
    class Positions(object):
        def __init__(self, position=None, count=None):
            self.position   = position
            self.count      = count
    
    positions = []
    
    for i in range(0,len(pos)):
        positions.append(Positions(pos[i]['roster_position']['position'],\
                                   pos[i]['roster_position']['count']))

    return positions;