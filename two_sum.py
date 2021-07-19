#array of nums, integer target
#return indices of two numbers in nums
#that sum up to target
#each input has exactly one solution

def twoSum(nums, target):

  hash_map = {}
  for index , value in enumerate(nums):
    if value not in hash_map:
      hash_map[value] = index
    else:
      return [hash_map[value], index]


nums = [-1,-2,-3,-4,-5]
target = -8
print(twoSum(nums,target))