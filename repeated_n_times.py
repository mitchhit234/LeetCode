from curses.ascii import NL


class Solution:

  def repeatedNTimes(self,nums):
    L = {}

    for i in nums:
      if i in L:
        return i
      else:
        L[i] = 1

    return -1





obj = Solution()
nums = [1,2,3,3]
print(obj.repeatedNTimes(nums))