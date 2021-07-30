#given a company with n employees, each with
#a unique id from 0 to n-1, the head of the company
#is the employee with headID
#each employee has a direct manager where manager[i]
#is the direct manager of the i-th employee
#return the number of minutes needed to inform all employees

def rec(head,dp,informTime):
  if head not in dp:
    return informTime[head]

  collect = []
  for i in dp[head]:
    collect.append(rec(i,dp,informTime))
  
  return max(collect) + informTime[head]
    


def numOfMinutes(n,headID,manager,informTime):
  if n < 2:
    return 0

  dp = {}
  for i in range(n):
    dp[manager[i]] = dp.get(manager[i],[]) + [i]

  time = rec(-1,dp,informTime)
  time -= informTime[-1]

  return time

    

n = 1
headID = 0
manager = [-1]
informTime = [0]
print(numOfMinutes(n,headID,manager,informTime))
