class Solution:
  #return the min number of fib numbers
  #that can sum up to k
  def findMinFibonacciNumbers(self,k):
    L = self.fib_up_to_n(k)
    i = len(L)-1
    current, count = 0, 0
    while current < k:
      while L[i] <= k - current:
        current += L[i]
        count += 1
      i -= 1

    return count


  def fib_up_to_n(self,n):
    start = [0,1]
    while start[-1] + start[-2] <= n:
      start.append(start[-1] + start[-2])
    return start[1:]

a = Solution()
k = 19
print(a.findMinFibonacciNumbers(k))