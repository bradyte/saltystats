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

#teamInfo    = yq.getTeamManagerInfoQuery(ls.team_id)

ls.week     = 12
ls.team_id  = 4
#teamRoster  = yq.getTeamWeeklyRosterQuery(ls.team_id)

#for i in range(len(teamRoster)):
#    data = pdb.selectEntryFromTable(match_column='player_id',match_value=teamRoster[i][0])
#    print(data)
#   
#29399
#9317
#30199 hunt downward trend
#6762 fitzgerald inconsistent
#29236 wentz very good
#28461 coleman consistent
ls.week = 12
#pid = 8565
#data = pdb.selectEntryFromTable(match_column='player_id',match_value=pid)[len(ls.statInfo[0]):]
#[sa, fpts] = yq.updatePlayerStatsQuery(pid)
#newData = pdb.selectEntryFromTable(match_column='player_id',match_value=pid)[len(ls.statInfo[0]):]
#for i in range(len(ls.statInfo[0])):
#    print('{}\t{}\t{:>}\t{:>}    \t{}'.format(i,sa[i],str(ls.statInfo[1][i]),str(ls.statName[i]),str(ls.statInfo[0][i])))

ids = pdb.selectAllPlayerIDs()
for i in range(1001,len(ids)):
    if ids[i] < 100000: # protect against defense ids
        yq.updatePlayerStatsQuery(ids[i])
#        if i % 10 == 0:
#            print('|',end='')


#pdb.updateTableEntry(index_column=ls.statName[0],match_column='player_id',match_value=pid,num=1)


####https://machinelearningmastery.com/feature-selection-machine-learning-python/



#newText = pdb.selectEntryFromTable(match_column='player_id',match_value=teamRoster[0][0])

#ls.week = 1
#for i in range(1,ls.leagueSettings.Dates.current_week):
#    ls.week = i
#    tmp = f.getPlayerStats(teamRoster[0][0])
#    print(tmp)


#tmp = nfl.playerDB[0:10]
#ls.week = 1
#for i in range(len(tmp)):
#f.updatePlayerStatsQuery(int(tmp[3][0]))

#with open('db/outfile.csv','r') as csvfile:
#    reader = csv.reader(csvfile)
#    tmpList = list(reader)[0]


#29399
#9317
#30199 hunt downward trend
#6762 fitzgerald inconsistent
#29236 wentz very good
#28461 coleman consistent


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

