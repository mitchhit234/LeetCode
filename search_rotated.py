#given an integer array nums sorted in
#ascending order with distinct values
#rotated at an unknown index
#given a target, return the index of the target 
#if it is in nums, otherwise return -1

def search(nums,target):
  if len(nums) == 1:
    if nums[0] == target:
      return 0
    else:
      return -1

  lo, hi, mid = 0, len(nums)-1, 0
  while lo < hi:
    mid = lo + (hi-lo)//2
    if nums[mid] > nums[hi]:
      lo = mid+1
    else:
      hi = mid
  
  rotation = lo

  lo, hi, mid = 0, len(nums)-1, 0
  while lo <= hi:
    mid = lo + (hi-lo)//2
    real_mid = (mid+rotation) % len(nums)
    if nums[real_mid] == target:
      return real_mid
    elif nums[real_mid] < target:
      lo = mid + 1
    else:
      hi = mid-1

  return -1



    




nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums,target))