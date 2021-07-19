#given n jobs and m workers and three arrays
#difficulty, profit, and worker,
#return the max profit we can achieve after assining
#the workers jobs

def maxProfitAssignment(difficulty, profit, worker):

  for i in range(len(difficulty)):
    difficulty[i] = [difficulty[i],profit[i]]

  difficulty = sorted(difficulty, key = lambda x: (x[0],-x[1]))

  mx = 0
  for i in range(len(difficulty)):
    mx = max(mx,difficulty[i][1])
    difficulty[i][1] = mx
    
  
  profit = 0
  for i in worker:
    low, high = 0, len(difficulty)-1
    while low < high:
      mid = low + (high-low)//2
      if difficulty[mid][0] < i and difficulty[mid+1][0] > i:
        low = mid
        high = mid
      elif difficulty[mid][0] < i:
        low = mid + 1
      elif difficulty[mid][0] > i:
        high = mid - 1
      else:
        low = mid
        high = mid
    if low == 0:
      if difficulty[low][0] <= i:
        profit += difficulty[low][1]
    else:
      profit += difficulty[low][1]




  return profit
    
        






difficulty = [68,35,52,47,86]
profit = [67,17,1,81,3]
worker = [92,10,85,84,82]
print(maxProfitAssignment(difficulty,profit,worker))
