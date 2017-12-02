import settings as ls
import yahooQuery as yq
import matplotlib.pyplot as plt
import pprint
import time
import playerDatabase as pdb
import numpy as np


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

#ls.week     = 12
ls.team_id  = 9
teamInfo    = yq.getTeamManagerInfoQuery(ls.team_id)
teamRoster  = yq.getTeamWeeklyRosterQuery(ls.team_id)



#for i in range(len(teamRoster)):
#    data = pdb.selectEntryFromTable(match_column='player_id',match_value=teamRoster[i][0])
#    print(data)
#   




#info = pdb.getSeasonPerformanceSQL(index_column = ls.statName[88], \
#                         match_column = ls.statName[83], match_value=teamRoster[0][0])
#
#
#weeks = [d[0] for d in info]
#stats = [d[1] for d in info]

#for i in range(1,ls.week):
#    table_name = 'stats_s' + str(ls.season) + 'w' + str(i)
#    pdb.createNewRowSQL(table_name)

names = []
totFpts = []
totCV = []
print('{:<20} {}\t{}\t{}'.format('Name','Avg','SD','CV'))

for j in range(len(teamRoster)):
    if teamRoster[j][1] != 'DEF' and teamRoster[j][2] != 'IR' and teamRoster[j][2] != 'BN':
        perf = []
        for i in range(1,ls.week):
            arr =    pdb.getWeeklyPositionPerformanceSQL(\
                    index_column='fpts', match_column='position', match_value=teamRoster[j][1], week=i)
            player = pdb.getWeeklyPlayerPerformanceSQL(\
                    index_column='fpts', match_column='player_id', match_value=teamRoster[j][0], week=i)
           
            if player != 'null':
                perf.append([i,player/np.max(arr)])
                
        pname = pdb.selectEntryFromTable(\
                    index_column='name',match_column='player_id',match_value=teamRoster[j][0])        
        names.append(pname)
        weeks = [d[0] for d in perf]
        stats = [d[1] for d in perf]
        #plt.plot(weeks,stats)
        #plt.axis([0, 17, 0, 1])
        #plt.title(pname)
        
        avg     = np.mean(stats)
        sd      = np.std(stats)
        cv      = sd/avg

        plt.scatter(cv,avg,color='red')
        plt.annotate(j+1,xy=(cv,avg),textcoords='offset points',xytext=(-10, 5),ha='right',\
                     arrowprops = dict(arrowstyle = 'fancy'))
        print('{:<3} {:<20} {:.3f}\t{:.3f}\t{:.3f}'.format(j+1,pname,avg,sd,cv))



plt.axis([0,1,0,1])
plt.show()




#perf = []
#for i in range(1,13):
#    arr =    pdb.getWeeklyPositionPerformanceSQL(index_column='fpts',match_column='position',\
#                                             match_value='WR',week=i)
#    player = pdb.getWeeklyPlayerPerformanceSQL(index_column='fpts', match_column='player_id',\
#                                           match_value=27624, week=i)
#    if player != 'null':
#        val = player/np.max(arr)
#        if val < 0: val = 0
#        perf.append([i,val])
#pname = pdb.selectEntryFromTable(index_column='name',match_column='player_id',match_value=27624)        
#weeks = [d[0] for d in perf]
#stats = [d[1] for d in perf]
#plt.plot(weeks,stats)
#plt.axis([0, 17, 0, 1])
#plt.title(pname)








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
 
print('\nExecution time: {}'.format(time.time() - tsys))
pdb.closeDatabase()

