#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 14:02:53 2018

@author: tombrady
"""

import yahooOauth2 as yo2
import json

baseURI         = 'https://fantasysports.yahooapis.com/fantasy/v2/'

###############################################################################
## jsonQuery
## input: query url, oauthToken
## output: result from query in raw JSON format
##
###############################################################################  
def jsonQuery(url):
    response = yo2.oauthToken.session.get(url)
    jsondata =json.loads(str(response.content,'utf-8'))
#    print(json.dumps(jsondata, indent=2))
    return jsondata

###############################################################################
## searchJSONObject
## searched JSON object for the provided string
## 
##
############################################################################### 
def searchJSONObject(jsondata, string):
    for d in jsondata:
        if string in d:
            return d[string]