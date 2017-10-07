getLeagueSize <- function(leagueURL, sig)
{
  leagueJSON  <- GET(paste0(leagueURL,"?format=json"),sig)
  leagueList  <- fromJSON(as.character(leagueJSON), asText=T)
  leagueSize  <- leagueList$fantasy_content$league[[1]]$num_teams
  
  return(leagueSize)
}

getYahooOAUTH1Signature <- function()
{
  t <- read.table("/Users/tbrady/.yahoo_key.txt")
  
  consumerKey    <- t[1,1]
  consumerSecret <- t[2,1]
  yahoo          <- oauth_endpoints("yahoo")
  
  myapp <- oauth_app("yahoo", key = consumerKey, secret = consumerSecret)
  token <- oauth1.0_token(yahoo, myapp)
  sig   <- sign_oauth1.0(myapp, token$oauth_token, token$oauth_token_secret)
  
  return(sig)
}

getGameKey <- function(baseURL)
{
  gameURL     <- paste0(baseURL,"game/nfl?format=json")
  gameJSON    <- GET(gameURL, sig)
  gameList    <- fromJSON(as.character(gameJSON), asText=T)
  gameKey     <- gameList$fantasy_content$game[[1]]$game_key
  
  return(gameKey)
}

getTeamNames <- function(baseURL)
{
  leagueJSON  <- GET(paste0(leagueURL,"?format=json"),sig)
  leagueList  <- fromJSON(as.character(leagueJSON), asText=T)
  leagueSize  <- leagueList$fantasy_content$league[[1]]$num_teams
  
  
}