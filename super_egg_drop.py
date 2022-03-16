import math

class Solution:
  def superEggDrop(self,k,n):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1, n+1):
      for j in range(1, k+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + 1
        if dp[i][j] >= n: 
          return i

obj = Solution()
k = 2
n = 6
print(obj.superEggDrop(k,n))