import cleaning
import settings as ls
import playerDatabase as pdb
from yahoo_oauth import OAuth2
import json


filePath = '/Users/tbrady/drive/sw/json/yahoo/oauth2.json'
baseURI = 'https://fantasysports.yahooapis.com/fantasy/v2/'

"""For your Oauth2 JSON file, please use the following format
  {
      "consumer_key":    "<CONSUMER_KEY>",
      "consumer_secret": "<CONSUMER_SECRET>",
  }
"""
oauthToken = OAuth2(None, None, from_file=filePath)
if not oauthToken.token_is_valid():
    oauthToken.refresh_access_token()



"""############################################################################
function - jsonQuery
desc -
input - query url, oauthToken
output - result from query in raw JSON format
"""
def jsonQuery(url):
    response = oauthToken.session.get(url)
    jsondata = json.loads(str(response.content, 'utf-8'))

    return jsondata


"""############################################################################
function - searchJSONObject
desc - searched JSON object for the provided string
input -
output -
"""
def searchJSONObject(jsondata, string):
    for d in jsondata:
        if string in d:
            return d[string]


"""############################################################################
function - getTeamManagerInfoQuery
desc -  This returns a manager class that has the roster based on team_id
input -
output -
"""
def getTeamManagerInfoQuery(team_id):
    url = baseURI + 'team/'\
        + str(ls.game_key) +'.l.' + str(ls.league_id) + '.t.' + str(team_id)\
        + '/roster;week=' + str(ls.week) + '?format=json'

    class ManagerInfo(object):
        def __init__(self, team_key=None, team_id=None, name=None,
                     waiver_priority=None, faab_balance=None,
                     number_of_moves=None, nickname=None):
            self.team_key = team_key
            self.team_id = team_id
            self.name = name
            self.waiver_priority = waiver_priority
            self.faab_balance = faab_balance
            self.number_of_moves = number_of_moves
            self.nickname = nickname

    jsondata = jsonQuery(url)
    tmp = jsondata['fantasy_content']['team'][0]

    mi = ManagerInfo()

    mi.team_key = searchJSONObject(tmp, 'team_key')
    mi.team_id = searchJSONObject(tmp, 'team_id')
    mi.name = searchJSONObject(tmp, 'name')
    mi.waiver_priority = searchJSONObject(tmp, 'waiver_priority')
    mi.faab_balance = searchJSONObject(tmp, 'faab_balance')
    mi.number_of_moves = searchJSONObject(tmp, 'number_of_moves')
    manager = searchJSONObject(tmp, 'managers')
    mi.nickname = manager[0]['manager']['nickname']

    return mi

"""############################################################################
function - getTeamWeeklyRosterQuery
desc - returns a roster object with the roster based on week and team_id
input -
output -
"""
def getTeamWeeklyRosterQuery(team_id):
    url = baseURI + 'team/'\
        + str(ls.game_key) +'.l.' + str(ls.league_id) + '.t.' + str(team_id)\
        + '/roster;week=' + str(ls.week) + '?format=json'

    jsondata    = jsonQuery(url)
    roster  = []

    for i in range(ls.roster_size):
        playerData = cleaning.cleanPlayerData(jsondata, i)
        player_id = searchJSONObject(playerData, 'player_id')
        selected_position = searchJSONObject(playerData, 'selected_position')
        display_position = searchJSONObject(playerData, 'display_position')
        roster.append([str(player_id),str(display_position), str(selected_position)])

    return roster


###############################################################################
## getWeeklyMatchups
##
##
##
###############################################################################
def getWeeklyMatchups():
    url = baseURI + 'leagues;league_keys=' \
        + str(ls.game_key) + '.l.' + str(ls.league_id)  \
        + '/scoreboard;week=' + str(ls.week) + '?format=json'

    jsondata = jsonQuery(url)
    tmp = jsondata['fantasy_content']['leagues']['0']['league'][1]['scoreboard']['0']['matchups']
    matchups = []
    for i in range(0,int(ls.num_teams/2)):
        team0 = tmp[str(i)]['matchup']['0']['teams']['0']['team'][0][1]['team_id']
        team0_pts = tmp[str(i)]['matchup']['0']['teams']['0']['team'][1]['team_points']['total']
        team1 = tmp[str(i)]['matchup']['0']['teams']['1']['team'][0][1]['team_id']
        team1_pts = tmp[str(i)]['matchup']['0']['teams']['1']['team'][1]['team_points']['total']
        matchups.append([int(team0), float(team0_pts), int(team1), float(team1_pts)])

    return matchups

###############################################################################
## getPlayerStats
##
##
##
###############################################################################
def getPlayerStatsQuery(player_id):
    url         = baseURI + 'player/' \
                + str(ls.game_key) + '.p.' + str(player_id)\
                + '/stats;week=' + str(ls.week)\
                +'?format=json'
    jsondata = jsonQuery(url)

    byeWeek     = searchJSONObject(jsondata['fantasy_content']['player'][0], 'bye_weeks')
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

        return tmpStats


###############################################################################
## getPlayerInfoQuery
##
##
##
###############################################################################
def getPlayerInfoQuery(player_id):
    url = baseURI + 'player/' \
        + str(ls.game_key) + '.p.' + str(player_id)\
        + '/stats;week=' + str(ls.week) +'?format=json'

    jsondata    = jsonQuery(url)
    team_id     = 0
    name        = None
    position    = None
    team_abbr   = None

    if 'error' in jsondata:
        print('Player does not exist')
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
## getLeagueTransactionQuery
##
##
##
###############################################################################
def getLeagueTransactionQuery():
    url         = baseURI + 'leagues;league_keys=' \
                + str(ls.game_key) + '.l.' + str(ls.league_id) \
                + '/transactions?format=json'
    jsondata    = jsonQuery(url)
    tx  = jsondata['fantasy_content']['leagues']['0']['league'][1]['transactions']



###############################################################################
## getPlayerStats
##
##
##
###############################################################################
def updatePlayerStatsQuery(player_id, table_name, update):
    url         = baseURI + 'player/'\
                + str(ls.game_key) + '.p.' + str(player_id)\
                + '/stats;type=week;week=' + str(ls.week)\
                +'?format=json'


    jsondata    = jsonQuery(url)

    byeWeek     = searchJSONObject(jsondata['fantasy_content']['player'][0], 'bye_weeks')
    byeWeek     = int(byeWeek['week'])

    tmpStats    = jsondata['fantasy_content']['player'][1]['player_stats']['stats']
    statsArray  = [0] * (len(ls.statInfo[0])) #create blank array
    fpts        = 0

    if ls.week == byeWeek:
        statsArray[0]  = 'BYE'
    else:
        for j in range(1,len(ls.statInfo[0])): # clear out array just in case
            if update:
                pdb.updateTableEntry(table_name     = table_name,
                                     index_column   = ls.statName[j],
                                     match_column   = 'player_id',
                                     match_value    = player_id,
                                     num            = 0)

        for i in range(0,len(tmpStats)): # update the individual stats column
            if update:
                stat_id                             = int(tmpStats[i]['stat']['stat_id'])
                statsArray[stat_id]                 = int(tmpStats[i]['stat']['value'])
                pdb.updateTableEntry(table_name     = table_name,
                                     index_column   = ls.statName[stat_id],
                                     match_column   = 'player_id',
                                     match_value    = player_id,
                                     num            = statsArray[stat_id])

        for i in range(len(ls.statInfo[1])): # update the fpts value
            if update:
                fpts += ls.statInfo[1][i]*statsArray[i]
                pdb.updateTableEntry(table_name     = table_name,
                                     index_column   = 'fpts',
                                     match_column   = 'player_id',
                                     match_value    = player_id,
                                     num            = fpts)

    return [statsArray, fpts]



def checkForBYE(player_id):
    url         = baseURI + 'player/'\
                + str(ls.game_key) + '.p.' + str(player_id)\
                + '/stats;?format=json'

    jsondata    = jsonQuery(url)

    byeWeek     = searchJSONObject(jsondata['fantasy_content']['player'][0], 'bye_weeks')
    byeWeek     = int(byeWeek['week'])

    return byeWeek


