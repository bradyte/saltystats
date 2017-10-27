from func import getGameKey, getWeeklyRoster, printCleanRoster, beginOauth2Session


oauthToken  = beginOauth2Session()

game_key    = getGameKey(oauthToken)
league_id   = 470610
team_id     = 1
week        = 1

roster      = getWeeklyRoster(game_key, league_id, team_id, week, oauthToken)
printCleanRoster(roster)

#leagueSettings = getLeagueSettings(game_key,league_id)




