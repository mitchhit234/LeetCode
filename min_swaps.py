class Solution:


  def minSwaps(self,nums):
    ones = nums.count(1)
    nums = nums + nums
    x, onesInWindow = 0, 0
    for i in range(len(nums)):
      if i >= ones and nums[i - ones]:
        x -= 1
      if nums[i] == 1:
        x += 1
      onesInWindow = max(x,onesInWindow)
    return ones - onesInWindow



obj = Solution()
nums = [0,1,0,1,1,0,0]
#nums = [0,1,1,1,0,0,1,1,0]
print(obj.minSwaps(nums))