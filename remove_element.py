#given an integer array of nums and
#an integer val, use in space operations
#to remove all instances of val from nums
#return the length of the final array

def removeElement(nums, val):
  i = 0
  for num in nums:
    if num != val:
      nums[i] = num
      i += 1
  return i



removeElement([3,2,2,3],2)