import math
class Solution:
  def consecutiveNumbersSum(self, n):
    count = 1
    for i in range(2,math.ceil(math.sqrt(2*n))):
      if (n - (i * (i+1))/2) % i == 0:
        count += 1

    return count



obj = Solution()
n = 5
print(obj.consecutiveNumbersSum(n))
        