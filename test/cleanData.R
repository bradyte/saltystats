setwd("~/drive/sw")
library(ggplot2)
source("func.R")

# https://www.datacamp.com/community/tutorials/r-tutorial-apply-family#codelapplycode
# http://www.footballdb.com/fantasy-football/index.html


lsz = 10 # league size, future proof
scor = read.csv(file="qb_rb_wr_te_scoring.csv",head=TRUE,sep=",",stringsAsFactors = FALSE)

# get qb info
setwd("~/drive/sw/qb")               # change dir to qb csv folder
qbfiles = list.files(pattern="*.csv") # find all csv file names
qb = list()                         # initialize the qb list
for (i in 1:length(qbfiles)) { qb[[i]] = read.csv(qbfiles[i]) } # read in the files to a multidimensional list

# get rb info
setwd("~/drive/sw/rb")               # change dir to qb csv folder
rbfiles = list.files(pattern="*.csv") # find all csv file names
rb = list()                         # initialize the qb list
for (i in 1:length(rbfiles)) { rb[[i]] = read.csv(rbfiles[i]) } # read in the files to a multidimensional list



setwd("~/drive/sw")                          # move back to original directory

qbTiers   = calcFptsReorder(qb, scor) # apply the scoring values then sum the total points and reorder most to least
# QB1tier0  = returnTierAverage(qbTiers, 0*lsz+1)
# QB1tier1  = returnTierAverage(qbTiers, 1*lsz+1)
# QB1tier2  = returnTierAverage(qbTiers, 2*lsz+1)

rbTiers  = calcFptsReorder(rb, scor) # apply the scoring values then sum the total points and reorder most to least
# RBtier0  = (returnTierAverage(rbTiers, 0*lsz+1) + returnTierAverage(rbTiers, 0*lsz+2))/2
# RBtier1  = returnTierAverage(rbTiers, 1*lsz+1)
# RBtier2  = returnTierAverage(rbTiers, 2*lsz+1)
# RBtier3  = returnTierAverage(rbTiers, 3*lsz+1)
# RBtier4  = returnTierAverage(rbTiers, 4*lsz+1)


