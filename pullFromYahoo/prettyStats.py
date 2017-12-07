#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:54:38 2017

@author: tbrady
"""
import playerDatabase as pdb
import settings as ls
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import yahooQuery as yq
from scipy.stats import norm

def plotTeamPDF(teamRoster):

    team_mu     = []
    team_var    = []
    teamInfo    = yq.getTeamManagerInfoQuery(ls.team_id)
    for idx in range(len(teamRoster)):
        if  teamRoster[idx][1] != 'DEF' and\
            teamRoster[idx][2] != 'IR'  and\
            teamRoster[idx][2] != 'BN':
            mu      = 0
            weeks   = []
            stats   = []
            perf    = []
            for i in range(1,ls.week-1):
                arr = pdb.getWeeklyPositionPerformanceSQL(index_column='fpts',match_column='position',\
                                                         match_value=teamRoster[idx][1],week=i)
                player = pdb.getWeeklyPlayerPerformanceSQL(index_column='fpts', match_column='player_id',\
                                                       match_value=teamRoster[idx][0], week=i)
                if player != 'null':
#                   val = player/max(arr)
#                   if val < 0: val = 0
                    perf.append([i,player])
#                pname = pdb.selectEntryFromTable(index_column='name',match_column='player_id',match_value=teamRoster[idx][0])        
            weeks = [d[0] for d in perf]
            stats = [d[1] for d in perf]
                
            mu = np.mean(stats)
            var = np.var(stats)
            
            team_mu.append(mu)
            team_var.append(var)

    
    mu = np.sum(team_mu)
    sigma = np.sqrt(np.mean(team_var))
    
    x       = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    pdf     = mlab.normpdf(x, mu, sigma)
    plt.plot(x,pdf)
    plt.annotate(teamInfo.nickname,
                 xy=(mu,max(pdf)),
                 xytext=(mu*0.9,mu/1000),
                 arrowprops=dict(arrowstyle='-'))
    return [mu, sigma]

    
def getOutcomeProbabilities(mu1, mu2, sigma1, sigma2):
    A =          1/(sigma2**2) -        1/(sigma1**2)
    B =      2*mu1/(sigma1**2) -    2*mu2/(sigma2**2)
    C =   (mu2**2)/(sigma2**2) - (mu1**2)/(sigma1**2) - 2*np.log(sigma1/sigma2)
    
    rts = np.roots([A, B, C])
    
    if mu1 > mu2:
        muW = mu1
        sigmaW = sigma1
        muL = mu2
        sigmaL = sigma2
    else:
        muW = mu2
        sigmaW = sigma2
        muL = mu1
        sigmaL = sigma1
    
    
    if ((rts[0] > mu1 and rts[0] < mu2) or (rts[0] > mu2 and rts[0] < mu1)):
        x0 = rts[0]
    elif((rts[1] > mu1 and rts[1] < mu2) or (rts[1] > mu2 and rts[1] < mu1)):
        x0 = rts[1]
    
    plt.axvline(x=x0,color='r')
    
    
    
    
    w_error    = norm.cdf(x0, muW, sigmaW)    
    w_perc     = 1-w_error
    l_perc = norm.cdf(x0, muL, sigmaL)
    
    print('Winner Probability: {}'.format(w_perc))

    
    
    
    
    
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