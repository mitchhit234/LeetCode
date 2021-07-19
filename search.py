#given an array of integers nums which
#is sorted in ascending order,
#return the index of the integer
#target in nums if it exists, otherwise
#return -1

def search(nums,target):
  lower, upper = 0, len(nums)-1

  while lower <= upper:
    mid = lower + ((upper-lower)//2)
    if nums[mid] < target:
      lower = mid+1
    elif nums[mid] > target:
      upper = mid-1
    else:
      return mid
  
  return -1



n = [5]
t = 5
print(search(n,t))