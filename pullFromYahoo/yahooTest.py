import settings as ls
import yahooQuery as yq
import matplotlib.pyplot as plt
import prettyStats as ps
import time
import playerDatabase as pdb
import numpy as np
import matplotlib.mlab as mlab
import history as hs
import defenses as d

tsys = time.time()

# https://developer.yahoo.com/yql/console/
# http://jsonviewer.stack.hu/
# https://jsonformatter.curiousconcept.com/
# https://machinelearningmastery.com/feature-selection-machine-learning-python/
# https://www.kaggle.com/mashimo/features-selection-for-multiple-linear-regression

# 29399
# 9317
# 30199 hunt downward trend
# 6762 fitzgerald inconsistent
# 29236 wentz very good
# 28461 coleman consistent
# pid = 8565

ls.week = ls.leagueSettings.Dates.current_week

ls.team_id = 10
#idx = 0
teamInfo = yq.getTeamManagerInfoQuery(ls.team_id)
teamRoster = yq.getTeamWeeklyRosterQuery(ls.team_id)
for idx in range(15):
    pos = teamRoster[idx][1]
    if pos != 'K' or pos != 'DEF':
        player_id = teamRoster[idx][0]
        bye_week = yq.checkForBYE(player_id)
        perf = [[0,0]] # padding index 0

        for wk in range(1,ls.week):
            if wk != bye_week:
                tmp = pdb.getWeeklyPlayerPerformanceSQL(
                        index_column = 'fpts',
                        match_column = 'player_id',
                        match_value = player_id,
                        week = wk)
                perf.append([wk,tmp])

        weeks = [d[0] for d in perf]
        X = [d[1] for d in perf]



        pname = pdb.selectEntryFromTable(
                index_column = 'name',
                match_column = 'player_id',
                match_value = player_id)
#        plt.figure(figsize=(8,4))
#        plt.title(pname)
#        plt.plot(weeks[1:], X[1:], marker='o', color='k', label='Xn, Weekly Performance')
#        plt.xlim([0,17])
#        plt.xlabel('NFL Week')
#        plt.ylim([0,50])
#        plt.ylabel('Fantasy Points')
#        plt.grid(True)
#        ps.plotPositionRanges(pos)


        if pos == 'WR' or pos == 'RB':
            a0 = d.getCurrentOpponentPerformance(player_id, pos)
            a0 = a0/2
            a_prev = d.getPlayerAgainstDefensePerformance(player_id, pos)
            a_prev = list(np.divide(a_prev,2))
            a_prev.append(a0)
        else:
            a0 = d.getCurrentOpponentPerformance(player_id, pos)
            a_prev = d.getPlayerAgainstDefensePerformance(player_id, pos)
            a_prev.append(a0)

        if weeks[1] == 1:
            week1 = 2
        else:
            week1 = 1
        cur = weeks[week1:]
        cur.append(ls.week)
#        plt.plot(cur, a_prev[2:], linestyle=':', marker='.', color='b', label='an, Defense Strength')


        pred = [0, 0] # ignore week 0, 1
        error = [0, 0] # ignore week 0, 1
        w0 = 1
        weights = [0, w0]
        for i in range(week1,len(X)):
            err = 0
            Y = a_prev[i] * w0
            if Y < 0:
                Y = 0
            pred.append(Y)
            if X[i] > 1:
                err = (X[i] - pred[i]) / X[i]
                error.append(err)
                w0 = w0 + err
                weights.append(w0)
            else:
                w0 = 1


        avg_error = np.mean(np.abs(error))
        Xn = w0*a0
        pred.append(Xn)
#
#        plt.plot(cur,pred[2:],color='r', label='Yn, Weekly Prediction')
#        plt.legend()
#        plt.show()
#        print('Week 15 prediction: {:.3f}'.format(Xn))


    #
    #    plt.figure(figsize=(8,2))
    #    plt.xlim([0,17])
    #    plt.xlabel('NFL Week')
    #    plt.bar(weeks[2:], error[2:])
    #    plt.ylim([-1,1])
    #    plt.ylabel('Error Percentage')
    #    plt.grid(True)
    #    plt.show()
        print('{}\t{:.3f}'.format(pos,(1-avg_error)*100))


print('\nExecution time: {:.6f}s'.format(time.time() - tsys))
pdb.closeDatabase()
