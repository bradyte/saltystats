import json  
from yahoo_oauth import OAuth2


def beginOauth2Session():
    oauth = OAuth2(None, None, from_file='oauth2.json')
    if not oauth.token_is_valid():
        oauth.refresh_access_token()
    return oauth;
    
def jsonQuery(url, oauthToken) :
    #json viewer http://jsonviewer.stack.hu/
    #json formatter https://jsonformatter.curiousconcept.com/
    response = oauthToken.session.get(url)
    jsondata =json.loads(str(response.content,'utf-8'))
    #print(json.dumps(jsondata, indent=2))
    return jsondata;

def getGameKey(oauthToken):
    #nfl_game_id
    #2001 - 57
    #2002 - 49
    #2003 - 79
    #2004 - 101
    #2005 - 124
    #2006 - 153
    #2007 - 175
    #2008 - 199
    #2009 - 222
    #2010 - 242
    #2011 - 257
    #2012 - 273
    #2014 - 331
    #2015 - 348
    #2016 - 359
    #2017 - 371
    url = 'https://fantasysports.yahooapis.com/fantasy/v2/game/nfl?format=json'
    jsondata = jsonQuery(url, oauthToken)
    return jsondata['fantasy_content']['game'][0]['game_key'];
  
 
def YahooIsGarbage(jsondata, i):
    class Struct(object):
            def __init__(self, **entries):
                self.__dict__.update(entries)
    
    playerData0 = jsondata['fantasy_content']['teams']['0']['team'][1]['roster']['0']['players'][str(i)]['player'][0]
    tmp         = jsondata['fantasy_content']['teams']['0']['team'][1]['roster']['0']['players'][str(i)]['player'][1]
    tmp         = Struct(**tmp)
    playerData1 = tmp.selected_position
    playerData  = playerData0 + playerData1
    return playerData;

def getWeeklyRoster(game_key, league_id, team_id, week, oauthToken):
    url     = 'https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys='  \
                + str(game_key) +'.l.' + str(league_id) + '.t.' + str(team_id) + \
                '/roster;week='+str(week)+'?format=json'
                        
    jsondata = jsonQuery(url, oauthToken)
    
    roster = [];
    
    class Player(object):
        def __init__(self, player_id, name_full, editorial_team_abbr, \
                     display_position, elected_position=None):
            self.player_id              = player_id
            self.name_full              = name_full
            self.editorial_team_abbr    = editorial_team_abbr
            self.display_position       = display_position
            self.selected_position      = selected_position
            
    for i in range(0,14):
        playerData          = YahooIsGarbage(jsondata, i)
        player_id           = [d['player_id']           for d in playerData if 'player_id'              in d][0]
        name_full           = [d['name']['full']        for d in playerData if 'name'                   in d][0]
        editorial_team_abbr = [d['editorial_team_abbr'] for d in playerData if 'editorial_team_abbr'    in d][0]
        display_position    = [d['display_position']    for d in playerData if 'display_position'       in d][0]
        selected_position   = [d['position']            for d in playerData if 'position'               in d][0]
        
        roster.append(Player(player_id, name_full, editorial_team_abbr, display_position, selected_position))

    return roster;

def getLeagueSettings(game_key, league_id, oauthToken):
    url     = 'https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=' \
                + str(game_key) + '.l.' + str(league_id) + '/settings?format=json'
                
    jsondata = jsonQuery(url, oauthToken)
    return jsondata;

def printCleanRoster(roster):
    print(    '{:<12} {:<24} {:<10} {:<10} {:<10}'.format(\
          'Player ID', 'Name', 'Team', 'Position', 'Roster'))
    
    for j in range(0,14):
        print('{:<12} {:<24} {:<10} {:<10} {:<10}'.format(\
              roster[j].player_id, \
              roster[j].name_full, \
              roster[j].editorial_team_abbr, \
              roster[j].display_position, \
              roster[j].selected_position))





