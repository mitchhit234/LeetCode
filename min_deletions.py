#return the min number of deletions
#so that no two letters have the same frequency
def minDeletions(s):
  #Grab counts, min, and mx
  L = {}
  for i in s:
    if i in L:
      L[i] += 1
    else:
      L[i] = 1
  
  N = [0]*max(L.values())

  #Organize in an array such that
  #the number of counts of length i are 
  #layed out next to each other
  for key in L:
    N[L[key]-1] += 1

  #Alter the array by only moving values down (deleting)
  #make it so every value is either a 1 or a 0
  count = 0
  for i in range(len(N)-1,0,-1):
    if N[i] > 1:
      count += N[i] - 1
      N[i-1] += N[i] - 1
  count += max(N[0] - 1,0)
    

  return count




s = "aab"
#s = "ceabaacb"
#s = "accdcdadddbaadbc"
print(minDeletions(s))