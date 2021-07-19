#Given a sorted array of distinct integers
#return the index where the target is found

def searchInsert(nums,target):
  if len(nums) == 1:
    if target > nums[0]:
      return 1
    else:
      return 0


  median_index = (len(nums)//2)
  if target < nums[median_index]:
    return searchInsert(nums[:median_index],target)

  elif target > nums[median_index]:
    return median_index + searchInsert(nums[median_index:],target)

  else:
    return median_index



nums=[1]
target=0
print(searchInsert(nums,target))