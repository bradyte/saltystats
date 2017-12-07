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




#week=ls.leagueSettings.Dates.current_week


#for i in range(1,11):
#    ls.team_id  = i
#    teamInfo    = yq.getTeamManagerInfoQuery(ls.team_id)
#    teamRoster  = yq.getTeamWeeklyRosterQuery(ls.team_id,week)
#    ps.plotTeamPDF(teamRoster)
#    print('.', end='')




#
#ls.team_id  = 3
#teamInfo    = yq.getTeamManagerInfoQuery(ls.team_id)
#teamRoster  = yq.getTeamWeeklyRosterQuery(ls.team_id,ls.week)
#[mu1, sigma1] = ps.plotTeamPDF(teamRoster)
#
#ls.team_id  = 10
#teamInfo    = yq.getTeamManagerInfoQuery(ls.team_id)
#teamRoster  = yq.getTeamWeeklyRosterQuery(ls.team_id,ls.week)
#[mu2, sigma2] = ps.plotTeamPDF(teamRoster)
#ps.getOutcomeProbabilities(mu1, mu2, sigma1, sigma2)
#
#
#plt.xlabel('Team Mean Points')
#plt.ylabel('PDF')
#plt.ylim([0,0.1])
#plt.show()

ls.week = 1
tmp = yq.getPlayerInfoQuery(26456)

#matchups = pdb.defCalcDefensivePerformance(1)





 
print('\nExecution time: {}'.format(time.time() - tsys))
pdb.closeDatabase()

