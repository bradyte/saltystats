calcFptsReorder = function(l, scor)
{
  # find the iteration variables
  ldims = length(l)
  # lrows = nrow(l[[1]])
  # lcols = ncol(l[[1]])
  # 
  # clear out all fpts values 
  for(i in 1:ldims) { l[[i]][, 4] = 0.0 }
  
  # apply the scoring values to all the stats then sum them together and iterate through players then years
  for(i in 1:ldims) {
    # for(j in 1:lrows) {
    #   for(k in 5:lcols) {
    #     l[[i]][j, fptsCol] <- l[[i]][j,fptsCol] + as.numeric(l[[i]][j,k]) * as.numeric(scor[k]) }
    # }
    l[[i]][,4] = apply(l[[i]][,5:20], 1, function(x) sum(x * data.frame(scor[1,5:20])))
  }

  for(i in 1:ldims) { l[[i]] = l[[i]][order(l[[i]]["fpts"], decreasing="true"), ] }   # reorder the list by fpts value from highest to lowest
  
  return(l)
}

returnTierAverage = function(l, tier)
{
  mean(as.double(lapply(l, '[[', tier, 4)))/16 #average the fpts of the player over all the years based on the rank
}
