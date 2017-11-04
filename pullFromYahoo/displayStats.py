###############################################################################
## printCleanRoster
## input: roster,class of classes
## output: a clean and formatted display of the roster query
##
############################################################################### 
def printCleanRoster(roster, roster_size):
    
    print('{:>12} {:<24} {:<10} {:<10} {:<10} {:>5}'.format(\
          'Player ID', 'Name', 'Team', 'Position', 'Roster', 'Fpts'))
    
    for i in range(0,roster_size):
        print('{:>12} {:<24} {:<10} {:<10} {:<10} {:>5.2f}'.format(\
              roster[i].player_id,              \
              roster[i].name_full,              \
              roster[i].editorial_team_abbr,    \
              roster[i].display_position,       \
              roster[i].selected_position,      \
              roster[i].player_points))

###############################################################################
## printCleanSettings
## input: 
## output: 
##
############################################################################### 
def printCleanSettings(leagueSettings, seeAbout, seeDates, seeScoring):
    
## prints about league  
    if seeAbout == 1:
        print('{:<22} {:<30}'.format('League Type:', leagueSettings.About.game_code.upper()))
        print('{:<22} {:<30}'.format('League Name:', leagueSettings.About.name))
        print('{:<22} {:<30}'.format('League Size:', leagueSettings.About.num_teams))
        print('{:<22} {:<30}'.format('League URL:' , leagueSettings.About.url))
        print('{:<20}'.format('Positions:'))

        for i in range(0, len(leagueSettings.About.roster_positions)):
            print(' {:<2}- {:<6}'.format(leagueSettings.About.roster_positions[i].count,\
                                         leagueSettings.About.roster_positions[i].position))
        print('\r')
        
## prints league dates
    if seeDates == 1:
        print('{:<22} {:<30}'.format('Season:', leagueSettings.Dates.season)) 
        print('{:<22} {:<30}\n'.format('Current Week:', leagueSettings.Dates.current_week))
        
## prints the scoring settings
    if seeScoring == 1:
        for k in range(0,len(leagueSettings.Scoring.statInfo.value)):
            if(leagueSettings.Scoring.statInfo.display_name[k] != None):
                print('{:-<20} {:6.2f}'.format(\
                      str(leagueSettings.Scoring.statInfo.display_name[k]), \
                      float(leagueSettings.Scoring.statInfo.value[k])))
                
###############################################################################
## printCleanMatchup
## input: 
## output: 
##
############################################################################### 
def printCleanMatchups(matchups, num_teams):
    
    for i in range(0,int(num_teams/2)):
        print('{:<24} {:<24} {:<24} {:<24} {:<24}'.format(\
              matchups[i].winner_team_key,  \
              matchups[i].team0_team_key,   \
              matchups[i].team0_total,      \
              matchups[i].team1_team_key,   \
              matchups[i].team1_total))
    