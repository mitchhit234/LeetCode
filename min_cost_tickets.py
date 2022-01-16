#return the min number of dollars
#needed to travel on every day given
def mincostTickets(days,costs):
  C = [0]*(days[-1]+1)
  L = {}
  for j in days:
    L[j] = 1  
  for i in range(1,days[-1]+1):
    if i in L:
      C[i] = min(C[i-1]+costs[0],C[max(0,i-7)]+costs[1],C[max(0,i-30)]+costs[2])
    else:
      C[i] = C[i-1]

  return C[days[-1]]



days = [1,4,6,7,8,20]
costs = [2,7,15]
print(mincostTickets(days,costs))