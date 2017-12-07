import settings as ls
import yahooQuery as yq
import matplotlib.pyplot as plt
import prettyStats as ps
import time
import playerDatabase as pdb
import numpy as np
import matplotlib.mlab as mlab

tsys = time.time()

## https://developer.yahoo.com/yql/console/
## http://jsonviewer.stack.hu/
## https://jsonformatter.curiousconcept.com/
####https://machinelearningmastery.com/feature-selection-machine-learning-python/
####https://www.kaggle.com/mashimo/features-selection-for-multiple-linear-regression

#29399
#9317
#30199 hunt downward trend
#6762 fitzgerald inconsistent
#29236 wentz very good
#28461 coleman consistent
#pid = 8565

ls.week     = 13
ls.team_id  = 5
teamInfo    = yq.getTeamManagerInfoQuery(ls.team_id)
teamRoster  = yq.getTeamWeeklyRosterQuery(ls.team_id)

player_id =3727

for i in range (1,13):
#    ls.week = i
#    table_name = 'stats_s' + str(ls.season) + 'w' + str(i) 
#    yq.updatePlayerStatsQuery(player_id, table_name)
    player = pdb.getWeeklyPlayerPerformanceSQL(index_column='fpts', match_column='player_id',\
                                                       match_value=player_id, week=i)   
    print(player)




#[mu1, sigma1] = ps.plotTeamPDF(teamRoster)
#
#ls.team_id  = 7
#teamRoster  = yq.getTeamWeeklyRosterQuery(ls.team_id)
#[mu2, sigma2] = ps.plotTeamPDF(teamRoster)
#ps.getOutcomeProbabilities(mu1, mu2, sigma1, sigma2)
#
#
#plt.ylim([0,0.1])
#plt.show()






 
print('\nExecution time: {}'.format(time.time() - tsys))
pdb.closeDatabase()

