#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:48:29 2017

@author: tbrady
"""
###############################################################################
## beginOauth2Session
## input: file path to the oauth.json file
## output: reusable token for queries to the Yahoo API
##
###############################################################################
from yahoo_oauth import OAuth2
import json  


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
def jsonQuery(url) :
    response = oauthToken.session.get(url)
    jsondata =json.loads(str(response.content,'utf-8'))
#    print(json.dumps(jsondata, indent=2))
    return jsondata;

###############################################################################
## getSeasonGameKey
## This is the key that identifies the fantasy season and fantasy sport
## Made by Yahoo but I had to brute force to get most of these numbers
##
############################################################################### 
def getSeasonGameKey():
##   season_ids
##   2001 - 57    2002 - 49    2003 - 79    2004 - 101   2005 - 124
##   2006 - 153   2007 - 175   2008 - 199   2009 - 222   2010 - 242
##   2011 - 257   2012 - 273   2013 - 314   2014 - 331   2015 - 348
##   2016 - 359   2017 - 371
    ids = [ 57,  49,  79, 101, 124, \
           153, 175, 199, 222, 242, \
           257, 273, 314, 331, 348, \
           359, 371]
    return ids[season - 2001]

  
    




season          = 2017
league_id       = 470610
team_id         = 1
week            = 1
game_key        = getSeasonGameKey()

filePath        = '/Users/tbrady/drive/sw/json/yahoo/oauth2.json'
oauthToken      = beginOauth2Session(filePath)






















