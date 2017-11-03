###############################################################################
## printCleanRoster
## input: roster,class of classes
## output: a clean and formatted display of the roster query
##
############################################################################### 
def printCleanRoster(roster, roster_size):
    
    print('{:>12} {:<24} {:<10} {:<10} {:<10} {:>5}'.format(\
          'Player ID', 'Name', 'Team', 'Position', 'Roster', 'Fpts'))
    
    for j in range(0,roster_size):
        print('{:>12} {:<24} {:<10} {:<10} {:<10} {:>5.2f}'.format(\
              roster[j].player_id,              \
              roster[j].name_full,              \
              roster[j].editorial_team_abbr,    \
              roster[j].display_position,       \
              roster[j].selected_position,      \
              roster[j].player_points))

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