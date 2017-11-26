#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:23:35 2017

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


def searchJSONObject(jsondata, string):
    for d in jsondata:
        if string in d:
            return d[string]





filePath        = '/Users/tbrady/drive/sw/json/yahoo/oauth2.json'
oauthToken      = beginOauth2Session(filePath)



