###############################################################################
## cleanPlayerData
## Meant to clean up the player data from four seperate lists into one list
##
##
############################################################################### 
def cleanPlayerData(d,i):
    d   = d['fantasy_content']['teams']['0']['team'][1]['roster']['0']['players'][str(i)]['player'] # strip the nonsense
    d0  = d[0] + [{'selected_position': d[1]['selected_position'][1]['position']}] # this makes a list entry     
    d0.append(dict(d[2])) # append the other two that are correct 
    d0.append(dict(d[3]))
    
    return d0


###############################################################################
## cleanPositions
## break up the two categories to index a lot more easily
## 
##
############################################################################### 
def cleanPositions(pos):
    
    positions   = []
    roster_size = 0
    
    for i in range(0,len(pos)):
        positions.append([pos[i]['roster_position']['position'], \
                          int(pos[i]['roster_position']['count'])])    
        if positions[i][0] != 'IR': # don't count IR spots for the official roster size
            roster_size += int(positions[i][1])

    return [positions, roster_size]

###############################################################################
## cleanStats
## Searches for stat info based on stat_id. Very confusing because the stat_id
## is not the index number so I make a new list indexed by the stat_id
##
############################################################################### 
def cleanStats(cats, mods):
    maxID = 0    
## get the last stat_id value, we only care about modifiers since those are
## used for scoring. there are stat_categories that have zero use but grab their
## names too
    for i in range(0,len(mods)):
        tmp = mods[i]['stat']['stat_id']
        if int(tmp) > maxID:
            maxID = tmp 
    for i in range(0,len(cats)):
        tmp = cats[i]['stat']['stat_id']
        if int(tmp) > maxID:
            maxID = tmp
        
## initialize arrays to use Yahoo's stupid stat_id as the index size
    stats  = [[None] * (maxID+1), [0] * (maxID+1)]
       
## use stat_id from the stat_modifiers to search the stat_categories  
    for i in range(0,len(cats)):
        idx             = cats[i]['stat']['stat_id']
        stats[0][idx]   = cats[i]['stat']['name']
## walk through the category list and only get categories that have modifiers
## associated with them        
        j       = 0
        tmpVal  = 0.0
        while(j < len(mods)):
            tmpMod = mods[j]['stat']['stat_id']
            if tmpMod == idx:
                tmpVal          = float(mods[j]['stat']['value'])
                stats[1][idx]   = tmpVal
            j += 1
        
    return stats;
                
