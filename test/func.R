calcFptsReorder = function(l)
{
  scor = read.csv(file="qb_rb_wr_te_scoring.csv",head=TRUE,sep=",",stringsAsFactors = FALSE)

  # get the number of dimensions (years) of the list
  ldims = length(l)

  # clear out all fpts values 
  for(i in 1:ldims) { l[[i]][, 4] = 0.0 }
  
  # apply the scoring values to all the stats then sum them together and iterate through players then years
  for(i in 1:ldims) { l[[i]][, 4] = apply(l[[i]][,5:20], 1, function(x) sum(x * data.frame(scor[1,5:20]))) }
  
  # reorder the list by fpts value from highest to lowest
  for(i in 1:ldims) { l[[i]]      = l[[i]][order(l[[i]]["fpts"], decreasing="true"), ] }
  return(l)
}

tieredPlot = function(meanMat,stdevMat)
{
  A = c(1:length(meanMat))
  
  df = data.frame(A, meanMat, stdevMat)

  q <- ggplot(df, aes(x = A,y = meanMat)) +
    geom_point() +
    geom_point(aes(colour = stdevMat, size = meanMat)) +
    scale_colour_gradient(high = "red", low = "green")
  plot(q)
}

readInRawStats = function(baseDir, folder)
{
  temp = list()                       # initialize the qb list
  setwd(paste(baseDir,folder,sep="")) # change dir to qb csv folder
  files = list.files(pattern="*.csv") # find all csv file names

  for (i in 1:length(files))
  {
    # read in the files to a multidimensional list
    temp[[i]] = read.csv(files[i])
  }
  return(temp)
}

returnTiersByMean = function(tiers)
{
  temp = matrix()
  k    = sapply(tiers, nrow)

  for(i in 1:k[1])
  {
    #average the fpts of the player over all the years based on the rank
    temp[i] =   mean(as.double(lapply(tiers, '[[', i, 4)))/16 
  }
  return(temp)
}

returnTiersByStdev = function(tiers)
{
  temp = matrix()
  k    = sapply(tiers, nrow)
  
  for(i in 1:k[1])
  {
    #stdev the fpts of the player over all the years based on the rank
    temp[i] =   sd(as.double(lapply(tiers, '[[', i, 4)))/16
  }
  return(temp)
}


