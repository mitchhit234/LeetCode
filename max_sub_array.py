#Given an integer array nums, find the
#find the subarray with the largest sum
#return that sum

def maxSubArray(nums):
  for i in range(1,len(nums)):
    nums[i] = max(nums[i], nums[i-1] + nums[i])
  return max(nums)
