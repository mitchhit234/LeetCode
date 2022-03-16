class Solution:

  def integerBreak(self,n):
    
    if n < 4:
      print (n)
      return n
    
    if n % 2 == 0:
      a = self.integerBreak(n//2)
      b = a
    else:
      a = self.integerBreak((n+1)//2)
      b = self.integerBreak((n-1)//2)

    return 0





n = 10
obj = Solution()
print(obj.integerBreak(n))