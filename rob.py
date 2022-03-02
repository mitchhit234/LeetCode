class Solution:
    def rob(self,nums):
      memo = [-1]*len(nums)
      return self.rec(memo,nums,len(nums)-1)


    def rec(self,memo,nums,index):
      if index < 0:
        return 0
      if memo[index] != -1:
        return memo[index]
      
      ret = max(self.rec(memo,nums,index-2)+nums[index],self.rec(memo,nums,index-1))
      memo[index] = ret
      return ret







obj = Solution()
nums = [1,2,3,1]
nums = [2,7,9,3,1]
print(obj.rob(nums))