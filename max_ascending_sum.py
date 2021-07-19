#given an array of positive integer nums
#return the max possible sum of an
#ascending subarray in nums

def maxAscendingSum(nums):
  mx, count = 0, nums[0]
  for i in range(1,len(nums)):
    if nums[i-1] < nums[i]:
      count += nums[i]
    else:
      mx = max(mx,count)
      count = nums[i]
  return max(mx,count)

n = [100,10,1]
print(maxAscendingSum(n))
