setwd("~/drive/sw")
library(ggplot2)
library(dplyr)
source("func.R")

# https://www.datacamp.com/community/tutorials/r-tutorial-apply-family#codelapplycode
# http://www.footballdb.com/fantasy-football/index.html

baseDir = "~/drive/sw/"
lsz = 10 # league size, future proof

# read in csv stats by folder name
qb = readInRawStats(baseDir, "qb")
rb = readInRawStats(baseDir, "rb")
wr = readInRawStats(baseDir, "wr")
te = readInRawStats(baseDir, "te")

# move back to original directory
setwd(baseDir)                          

# apply the scoring values then sum the total points and reorder most to least
qbTiersByYear   = calcFptsReorder(qb)
rbTiersByYear   = calcFptsReorder(rb)
wrTiersByYear   = calcFptsReorder(wr) 
teTiersByYear   = calcFptsReorder(te)

## TIERS for ten person league
# elite  = xxTiersMean[1]
# tier 1 = xxTiersMean[11]
# tier 2 = xxTiersMean[21]
# tier 3 = xxTiersMean[31] *rb/wr only
# tier 4 = xxTiersMean[41] *rb/wr only
# ten best available flex is flexTiersMean[41:50]


qbTiersMean     = returnTiersByMean(qbTiersByYear)
rbTiersMean     = returnTiersByMean(rbTiersByYear)
wrTiersMean     = returnTiersByMean(wrTiersByYear)
teTiersMean     = returnTiersByMean(teTiersByYear)
flexTiersMean   = sort(c(rbTiersMean, wrTiersMean, teTiersMean),decreasing = TRUE)

qbTiersStdev    = returnTiersByStdev(qbTiersByYear)
rbTiersStdev    = returnTiersByStdev(rbTiersByYear)
wrTiersStdev    = returnTiersByStdev(wrTiersByYear)
teTiersStdev    = returnTiersByStdev(teTiersByYear)
flexTiersStdev  = sort(c(rbTiersStdev, wrTiersStdev, teTiersStdev),decreasing = TRUE)


# tieredPlot(qbTiersMean, qbTiersStdev)
# plot(rbTiersMean)
# points(wrTiersMean, col= 2)
# points(teTiersMean, col= 3)
