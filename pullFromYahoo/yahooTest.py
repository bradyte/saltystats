from func import getGameKey, getWeeklyRoster, printCleanRoster


game_key    = getGameKey()
league_id   = 470610
team_id     = 1
week        = 1

roster      = getWeeklyRoster(game_key, league_id, team_id, week)
printCleanRoster(roster)

#leagueSettings = getLeagueSettings(game_key,league_id)




