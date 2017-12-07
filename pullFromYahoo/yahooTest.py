import settings as ls
import yahooQuery as yq
import matplotlib.pyplot as plt
import pprint
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
ls.team_id  = 1
teamInfo    = yq.getTeamManagerInfoQuery(ls.team_id)
teamRoster  = yq.getTeamWeeklyRosterQuery(ls.team_id)



#tmp = pdb.createAndUpdateWeekSQL(13)

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

#names = []
#totFpts = []
#totCV = []
#print('{:<20} {}\t{}\t{}'.format('Name','Avg','SD','CV'))
#
#for j in range(len(teamRoster)):
#    if teamRoster[j][1] != 'DEF' and teamRoster[j][2] != 'IR':# and teamRoster[j][2] != 'BN':
#        perf = []
#        for i in range(1,ls.week):
#            arr =    pdb.getWeeklyPositionPerformanceSQL(\
#                    index_column='fpts', match_column='position', match_value=teamRoster[j][1], week=i)
#            player = pdb.getWeeklyPlayerPerformanceSQL(\
#                    index_column='fpts', match_column='player_id', match_value=teamRoster[j][0], week=i)
#           
#            if player != 'null':
#                perf.append([i,player/np.max(arr)])
#                
#        pname = pdb.selectEntryFromTable(\
#                    index_column='name',match_column='player_id',match_value=teamRoster[j][0])        
#        names.append(pname)
#        weeks = [d[0] for d in perf]
#        stats = [d[1] for d in perf]
#        #plt.plot(weeks,stats)
#        #plt.axis([0, 17, 0, 1])
#        #plt.title(pname)
#        
#        avg     = np.mean(stats)
#        sd      = np.std(stats)
#        cv      = sd/avg
#
#        plt.scatter(cv,avg,color='red')
#        plt.annotate(j+1,xy=(cv,avg),textcoords='offset points',xytext=(-10, 5),ha='right',\
#                     arrowprops = dict(arrowstyle = 'fancy'))
#        print('{:<3} {:<20} {:.3f}\t{:.3f}\t{:.3f}'.format(j+1,pname,avg,sd,cv))
#
#
#
#plt.axis([0,1,0,1])
#plt.show()

plt.figure()
team_mu = []
team_sigma = []

idx = 1
for idx in range(len(teamRoster)):
    if teamRoster[idx][1] != 'DEF' and teamRoster[idx][2] != 'IR' and teamRoster[idx][2] != 'BN':
        mu      = 0
        sigma   = 0
        weeks   = []
        stats   = []
        perf    = []
        for i in range(1,ls.week):
            
            arr = pdb.getWeeklyPositionPerformanceSQL(index_column='fpts',match_column='position',\
                                                     match_value=teamRoster[idx][1],week=i)
            player = pdb.getWeeklyPlayerPerformanceSQL(index_column='fpts', match_column='player_id',\
                                                   match_value=teamRoster[idx][0], week=i)
            if player != 'null':
                perf.append([i,player])
            pname = pdb.selectEntryFromTable(index_column='name',match_column='player_id',match_value=teamRoster[idx][0])        
        weeks = [d[0] for d in perf]
        stats = [d[1] for d in perf]
            #plt.plot(weeks,stats)
            ##plt.axis([0, 17])
            #plt.title(pname)
            
        mu = np.mean(stats)
        sigma = np.std(stats)
        team_mu.append(mu)
        team_sigma.append(sigma)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x,mlab.normpdf(x, mu, sigma), color='red')

mu1 = np.sum(team_mu)
sigma1 = np.sum(sigma)


team_mu = []
team_sigma = []


teamRoster  = yq.getTeamWeeklyRosterQuery(5)

for idx in range(len(teamRoster)):
    if teamRoster[idx][1] != 'DEF' and teamRoster[idx][2] != 'IR' and teamRoster[idx][2] != 'BN':
        mu      = 0
        sigma   = 0
        weeks   = []
        stats   = []
        perf    = []
        for i in range(1,ls.week):
            
            arr = pdb.getWeeklyPositionPerformanceSQL(index_column='fpts',match_column='position',\
                                                     match_value=teamRoster[idx][1],week=i)
            player = pdb.getWeeklyPlayerPerformanceSQL(index_column='fpts', match_column='player_id',\
                                                   match_value=teamRoster[idx][0], week=i)
            if player != 'null':
                perf.append([i,player])
            pname = pdb.selectEntryFromTable(index_column='name',match_column='player_id',match_value=teamRoster[idx][0])        
        weeks = [d[0] for d in perf]
        stats = [d[1] for d in perf]
            #plt.plot(weeks,stats)
            ##plt.axis([0, 17])
            #plt.title(pname)
            
        mu = np.mean(stats)
        sigma = np.std(stats)
        team_mu.append(mu)
        team_sigma.append(sigma)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        plt.plot(x,mlab.normpdf(x, mu, sigma), color='blue')


mu2 = np.sum(team_mu)
sigma2 = np.sum(sigma)




plt.figure()
x1 = np.linspace(mu1 - 3*sigma1, mu1 + 3*sigma1, 100)
plt.plot(x1,mlab.normpdf(x1, mu1, sigma1), color='green')

x2 = np.linspace(mu2 - 3*sigma2, mu2 + 3*sigma2, 100)
plt.plot(x2,mlab.normpdf(x2, mu2, sigma2), color='red', linestyle='--')




plot.show()














#priors = [15.37, 12.11, 10.18, 8.9]
#t1 = []
#t2 = []
#t3 = []
#t4 = []
#tsp = []

#for i in range(len(stats)):
#    val = stats[i]
#    if val > priors[0]:
#        t1.append([weeks[i], stats[i]])
#    if val <= priors[0] and val > priors[1]:
#        t2.append([weeks[i], stats[i]])
#    if val <= priors[1] and val > priors[2]:
#        t3.append([weeks[i], stats[i]])
#    if val <= priors[2] and val > priors[3]:
#        t4.append([weeks[i], stats[i]])
#    if val <= priors[3]:
#        tsp.append([weeks[i], stats[i]])
#            
#        
#Pt1 = len(t1)/len(stats)
#Pt2 = len(t2)/len(stats)
#Pt3 = len(t3)/len(stats)
#Pt4 = len(t4)/len(stats)
#Ptsp = len(tsp)/len(stats)
#
#mu1 = np.mean([d[1] for d in t1])
#mu2 = np.mean([d[1] for d in t2])
#mu3 = np.mean([d[1] for d in t3])
##mu4 = np.mean([d[1] for d in t4])
#mutsp = np.mean([d[1] for d in tsp])
#
#idk = Pt1*mu1+Pt2*mu2+Pt3*mu3+Ptsp*mutsp#+Pt4*mu4





#    msd = 0
#    for i in range(len(stats)):
#    msd += stats[i] - np.mean(stats)
#    
#    msd /= len(stats)
    
#    
#plt.plot(x,mlab.normpdf(x, mu, sigma))
#plt.show()


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

