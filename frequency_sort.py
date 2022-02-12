import operator

class Solution:

  def frequencySort(self,nums):

    ret = []
    L = {}
    for i in nums:
      if i in L:
        L[i] += 1
      else:
        L[i] = 1


    for val in sorted(L.items(), key=lambda x: (x[1],-x[0])):
      for _ in range(L[val[0]]):
        ret.append(val[0])

    return ret


obj = Solution()
nums = [-1,1,-6,4,5,-6,1,4,1]
print(obj.frequencySort(nums))