# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import json
import xml.etree.ElementTree as etree
from yahoo_oauth import OAuth2
oauth = OAuth2(None, None, from_file='oauth2.json')


if not oauth.token_is_valid():
    oauth.refresh_access_token()
    
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
response = oauth.session.get(url)
xmldata = str(response.content,'utf-8')
print(xmldata)

#finally something useful
#https://developer.yahoo.com/fantasysports/guide/roster-resource.html

#root = etree.fromstring(xmldata)
#for child in root.iter():
#    print (child)
