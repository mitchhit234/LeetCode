

def findMin(nums):

  if nums[0] < nums[-1]:
    return nums[0]

  lo, hi = 0, len(nums)-1
  while lo < hi:
    mid = lo + (hi-lo)//2
    if nums[mid] >= nums[0]:
      lo = mid + 1
    else:
      hi = mid

  return nums[lo]








a = [2,1]
print(findMin(a))