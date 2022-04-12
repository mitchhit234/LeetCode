class Solution:

  def sumSubarrayMins(self, arr) -> int:
    tot = arr[0]
    mem = []

    for i in range(1,len(arr)):
      mem.append(min(arr[i-1],arr[i]))
      tot += arr[i] + mem[-1]

    while len(mem) > 1:
      tot, mem = self.merge(mem,tot)   

    return tot % (10**9 + 7)


  def merge(self,L,tot):
    new = []
    for i in range(1,len(L)):
      new.append(min(L[i-1],L[i]))
      tot += new[-1]

    return tot, new





obj = Solution()
arr = [3,1,2,4]
print(obj.sumSubarrayMins(arr))

