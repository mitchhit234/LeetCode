class Solution:


  def nthMagicalNumber(self,n,a,b):

    if n == 1:
      return min(a,b)

    a, b = min(a,b), max(a,b)
    g = self.gcd(a,b)
    lcm = (a*b) // g

    l, r = a, n*a
    while l <= r:
      mid = (l+r) // 2
      temp = self.magic_numbers_below(a,b,lcm,mid)
      if temp > n:
        r = mid
      elif temp < n:
        l = mid + 1
      else:
        l = r+1

    return (mid - min(mid % a, mid % b)) % (7 + 10**9)




  def gcd(self,a,b):
    if a % b == 0:
      return b
    else:
      return self.gcd(b,a%b)


  def magic_numbers_below(self,a,b,l,x):
    return (x // a) + (x // b) - (x // l)




obj = Solution()
n, a, b = 1000000000,40000,40000
print(obj.nthMagicalNumber(n,a,b))
