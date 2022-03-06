class Solution:
    def tribonacci(self, n) -> int:
      if n <= 0:
        return 0
      if n <= 2:
        return 1
      
      return self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)



obj = Solution()
n = 37
print(obj.tribonacci(37))




