import settings as ls
import yahooQuery as yq
import matplotlib.pyplot as plt
import pprint
import time
import playerDatabase as pdb
import os

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
pid = 8565

ls.week     = 1
ls.team_id  = 4
#teamInfo    = yq.getTeamManagerInfoQuery(ls.team_id)
#teamRoster  = yq.getTeamWeeklyRosterQuery(ls.team_id)

#for i in range(len(teamRoster)):
#    data = pdb.selectEntryFromTable(match_column='player_id',match_value=teamRoster[i][0])
#    print(data)
#   

#sql_string = 'INSERT INTO stats_s2017w2(active, pass_att) VALUES(0,0)'

#pdb.executeSQL(sql_string)

pdb.createSQLTable('stats_s2017w2')
#pdb.executeSQL('DROP TABLE stats_s2017w2')

#ids = pdb.selectAllPlayerIDs()
#for i in range(0,10):
#    if int(ids[i]) < 100000: # protect against defense ids
#        [statsArray, fpts] = yq.updatePlayerStatsQuery(ids[i])
#
#
#
#pdb.updateTableEntry(index_column=ls.statName[0],match_column='player_id',match_value=pid,num=1)































#fpts        = []
#fptsArr     = []
#fptsPlotArr = []
#fptsMean    = 0.0
#fptsStdev   = 0.0
#fptsCV      = 0.0
#fptsROC     = 0.0
#fptsPDF     = 0.0
#fptsSE      = 0.0 # standard error of mean
#fptsVar     = 0.0
#confInt     = 1.96  # z* of 95%
#confLimits  = 0.0


#print('Week:     Fpts      Average   Stdev     CV        ROC       Margin+/-') 
#for i in range(1, int(leagueSettings.Dates.current_week)):
#    fpts.append(getPlayerStats(season, player_id, i, leagueSettings.Scoring.statInfo.value, oauthToken))
#    if fpts[i-1] != 'BYE':
#        fptsArr.append(fpts[i-1])
#        fptsMean    = round(numpy.mean(fptsArr), 2)
#        fptsStdev   = round(numpy.std(fptsArr), 2)
#        if i == 1:
#            fptsCV      = 0.0
#            fptsROC     = 0.0
#            fptsEXP     = 0.0
#        else:
#            fptsCV      = round(fptsStdev/fptsMean, 2)
#            fptsROC     = round(fpts[i-1]/fptsMean, 2)
#            fptsSE      = round(confInt*fptsStdev/numpy.sqrt(i),2)
##            fptsVar     = round(fptsROC/fptsStdev,3)
#        plt.subplot(211)    
#        plt.scatter(i, fpts[i-1])
#        plt.xlabel('Week')
#        plt.title(title)
#        plt.axis([0, 17, 0, 40]) 
#        plt.grid(True)
#        
#        plt.subplot(212) 
#        plt.scatter(i, fptsVar)
#        plt.xlabel('Week')
#        plt.title('CV')
#        plt.axis([0, 17, 0, 0.6]) 
#        plt.grid(True)
#    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(\
#          i,fpts[i-1], fptsMean, fptsStdev, fptsCV, fptsROC, fptsSE))
#
# 
#
#plt.subplots_adjust(wspace=0.8, hspace=0.8)
#plt.show()
 
print('Execution time: {}'.format(time.time() - tsys))
pdb.closeDatabase()

