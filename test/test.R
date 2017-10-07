library("httr")
library("XML")
library("RJSONIO")
library("ggplot2")

source("func.R")

sig <- getYahooOAUTH1Signature()

baseURL  <- "http://fantasysports.yahooapis.com/fantasy/v2/"
leagueID <- "470610"
teamID   <- "1"
leagueSize  <- getLeagueSize(leagueURL,sig)
tn <- c()
for(i in 1:leagueSize)
{
  leagueKey   <- paste0(getGameKey(baseURL), ".l.", leagueID)
  teamKey     <- paste0(leagueKey, ".t.", i)
  teamURL     <- paste0(baseURL,"team/",teamKey)
  teamJSON  <- GET(paste0(teamURL,"?format=json"),sig)
  teamList  <- fromJSON(as.character(teamJSON), asText=T)

  tn[i] <- c(teamList$fantasy_content$team[[1]][[3]])
  print(tn[i])
}

