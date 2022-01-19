#given an array nums
#check if it can become non-decreasing
#by modifying at most one element
def checkPossibility(nums):
  changed = False
  for i in range(1,len(nums)):
    if nums[i-1] > nums[i]:
      if not changed:
        #try and change the previous value
        if i > 1:
          if i > 1 and nums[i-2] <= nums[i]:
            nums[i-1] = nums[i]
          #else default and change the current value
          else:
            nums[i] = nums[i-1]
        else:
          nums[i] = min(nums[i-1],nums[i])
          nums[i-1] = nums[i]
        changed = True
      else:
        return False
  
  return True


n = [3,4,2,3]
n = [4,2,3]
n = [1,4,1,2]
print(checkPossibility(n))
  
