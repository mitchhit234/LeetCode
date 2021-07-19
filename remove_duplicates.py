#remove integers from an array if they are 
#duplicates of previous values
#array input is in ascending order

def removeDuplicates(nums):
  i = 0
  for index in range(1,len(nums)):
    if nums[index] != nums[i]:
      i+=1
      nums[i] = nums[index]
  return i+1


print(removeDuplicates([1,1,2]))