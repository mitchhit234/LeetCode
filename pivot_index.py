
def pivotIndex(nums):

  total = sum(nums)
  current = 0
  for index in range(len(nums)):
    if current == total - current - nums[index]:
      return index
    current += nums[index]

  return -1




nums = [1,7,3,6,5,6]
print(pivotIndex(nums))