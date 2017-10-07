library("httr")
library("XML")
library("RJSONIO")
library("ggplot2")

t <- read.table("/Users/tbrady/.yahoo_key.txt")

consumerKey    <- t[1,1]
consumerSecret <- t[2,1]
yahoo          <- oauth_endpoints("yahoo")

myapp <- oauth_app("yahoo", key = consumerKey, secret = consumerSecret)
token <- oauth1.0_token(yahoo, myapp)
sig   <- sign_oauth1.0(myapp, token$oauth_token, token$oauth_token_secret)

baseURL  <- "http://fantasysports.yahooapis.com/fantasy/v2/"
leagueID <- "470610"

gameURL     <- paste0(baseURL,"game/nfl?format=json")
gameKeyJSON <- GET(gameURL, sig)
gameKeyList <- fromJSON(as.character(gameKeyJSON), asText=T)
gameKey     <- gameKeyList$fantasy_content$game[[1]]["game_key"]

leagueKey   <- paste0(gameKey, ".l.", leagueID)
leagueURL   <- paste0(baseURL,"league/")
teamURL     <- paste0(baseURL,"team/")

myTeamID        <- "1"
myTeamKey       <- paste0(leagueKey, ".t.", myTeamID)
myTeamURL       <- paste0(teamURL, myTeamKey, "/stats?format=json")
myTeamStatsJSON <- GET(myTeamURL, sig)
myTeamList      <- fromJSON(as.character(myTeamStatsJSON), asText=T)