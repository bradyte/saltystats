import json
from yahoo_oauth import OAuth2
oauth = OAuth2(None, None, from_file='oauth2.json')


if not oauth.token_is_valid():
    oauth.refresh_access_token()
 
    
    
def YahooIsGarbage(jsondata, i):
    class Struct(object):
            def __init__(self, **entries):
                self.__dict__.update(entries)
    
    playerData0 = jsondata["fantasy_content"]["teams"]["0"]["team"][1]["roster"]["0"]["players"][str(i)]["player"][0]
    tmp         = jsondata["fantasy_content"]["teams"]["0"]["team"][1]["roster"]["0"]["players"][str(i)]["player"][1]
    tmp         = Struct(**tmp)
    playerData1 = tmp.selected_position
    playerData = playerData0 + playerData1
    return playerData;



url      = "https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys=371.l.470610.t.1/roster;week=3?format=json"
response = oauth.session.get(url)
jsondata =json.loads(str(response.content,'utf-8'))


for i in range(0,14):
    playerData          = YahooIsGarbage(jsondata, i)
    player_id           = [d['player_id']           for d in playerData if 'player_id'              in d][0]
    name_full           = [d['name']['full']        for d in playerData if 'name'                   in d][0]
    editorial_team_abbr = [d['editorial_team_abbr'] for d in playerData if 'editorial_team_abbr'    in d][0]
    display_position    = [d['display_position']    for d in playerData if 'display_position'       in d][0]
    selected_position   = [d['position']            for d in playerData if 'position'               in d][0]
    
    
    jsonstr = "%s\t%s\t\t%s\t%s\t%s\t\r" % (player_id, name_full, editorial_team_abbr, display_position, selected_position)
    print(jsonstr)





#url = "https://fantasysports.yahooapis.com/fantasy/v2/game/nfl?format=json"
#response = oauth.session.get(url)
#jsondata =json.loads(str(response.content,'utf-8'))
    
    
#275585
#470610
#26777
#get Chris Thompson
#url = "https://fantasysports.yahooapis.com/fantasy/v2/players;player_keys=371.p.26777"
#get league info
#url = "https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=371.l.470610"
#url = "https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=371.l.470610/settings"
#url = "https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=371.l.470610/players;player_keys=371.p.26777/ownership"

#get the roster by week
#this will allow me to get players on teams
#url = "https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys=371.l.470610.t.1/roster;week=5"


#print(json.dumps(playerData, indent=2))
#print(selected_position[1]['position'])
#searchParam = 

#for i in range(0,14):
###    player_key          = jsondata["fantasy_content"]["teams"]["0"]["team"][1]["roster"]["0"]["players"][str(i)]["player"][0][0]["player_key"]
###    player_id           = jsondata["fantasy_content"]["teams"]["0"]["team"][1]["roster"]["0"]["players"][str(i)]["player"][0][1]["player_id"]
#    name_full           = jsondata["fantasy_content"]["teams"]["0"]["team"][1]["roster"]["0"]["players"][str(i)]["player"][0][2]["name"]["full"]
#    position            = jsondata["fantasy_content"]["teams"]["0"]["team"][1]["roster"]["0"]["players"][str(i)]["player"][0][9]
####    selected_position   = jsondata["fantasy_content"]["teams"]["0"]["team"][1]["roster"]["0"]["players"][i]["player"][1]["selected_position"][1]["position"]
##    selected_position = jsondata["fantasy_content"]["teams"]["0"]["team"][1]["roster"]["0"]["players"][str(i)]["player"][1]["selected_position"]#[1]["position"]
#    jsonstr = "%s\t%s\t\r" % (name_full, position)
####    jsonstr = "%s\t%s\t%s\t%s\r" % (player_id, name_full, position, selected_position)
#    print(jsonstr)


#finally something useful
#https://developer.yahoo.com/fantasysports/guide/roster-resource.html


