#input n stairs to reach the top
#you can climb one or two stairs at 
#a time, output the total number
#of ways to climb the stairs

def climbStairs(n):
  if n <= 1:
    return n
  
  dp = [1,2]
  for i in range(2,n):
    dp.append(dp[i-1] + dp[i-2])

  return dp[n-1]






print(climbStairs(6))