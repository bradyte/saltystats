###############################################################################
## cleanPlayerData
## Meant to clean up the player data from four seperate lists into one list
##
##
############################################################################### 
def cleanPlayerData(d,i):
    tmp = d['fantasy_content']['teams']['0']['team']
    d   = tmp[1]['roster']['0']['players'][str(i)]['player']
    
    d0  = d[0] + [{'selected_position': d[1]['selected_position'][1]['position']}]
    d0.append(dict(d[2]))
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
        positions.append([pos[i]['roster_position']['position'], int(pos[i]['roster_position']['count'])])
        if positions[i][0] != 'IR':
            roster_size += int(positions[i][1])

    return [positions, roster_size]

###############################################################################
## cleanStats
## Searches for stat info based on stat_id. Very confusing because the stat_id
## is not the index number so I make a new list indexed by the stat_id
##
############################################################################### 
def cleanStats(mods, cats):

## oddly enough, these aren't always equal
    lenModifiers = len(mods)
    lenCategories = len(cats)
    maxID = 0
    
## get the last stat_id value, we only care about modifiers since those are
## used for scoring. there are stat_categories that have zero use    
    for i in range(0,lenModifiers):
        tmp = mods[i]['stat']['stat_id']
        if int(tmp) > maxID:
            maxID = tmp  
        
    class StatInfo(object):
        def __init__(self, display_name=None, value=None):
            self.display_name   = display_name
            self.value          = value
    
    statInfo = StatInfo()
    
## initialize arrays to use Yahoo's stupid stat_id as the index size
    statInfo.display_name   = [None] * (maxID+1)
    statInfo.value          =    [0] * (maxID+1)
       
## use stat_id from the stat_modifiers to search the stat_categories  
    for i in range(0,lenModifiers):
        statIndex = mods[i]['stat']['stat_id']
        statInfo.value[statIndex] = float(mods[i]['stat']['value'])
## walk through the category list and only get categories that have modifiers
## associated with them        
        j = 0
        while(j < lenCategories):
            tmpCat = cats[j]['stat']['stat_id']
            if tmpCat == statIndex:
               statInfo.display_name[statIndex] = cats[j]['stat']['display_name']
            j += 1

    return statInfo;
                
