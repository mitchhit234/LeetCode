#The beauty of an index is equal to
#2 if all indicies less than are less than
#its value, and all incidies greater than are greater
#than its value
#1 if at least the neighbor indicies satisfy that rule,
#but not all indicies
#0 otherwise

def sumOfBeauties(nums):
  beauty = 0

  left, right = [nums[0]], [nums[len(nums)-1]]

  for i in range(1,len(nums)):
    left.append(max(left[i-1],nums[i]))
  
  for ix, val in enumerate(nums[::-1][1:]):
    right.append(min(right[ix],val))
  right = right[::-1]
    
  for i in range(1,len(nums)-1):
    if left[i-1] < nums[i] < right[i+1]:
      beauty += 2
    elif nums[i-1] < nums[i] < nums[i+1]:
      beauty += 1
  
  return beauty


    


# def sumOfBeauties(nums):
#   beauty = 0
#   for i in range(1,len(nums)-1):
#     current = nums[i]
#     j, k = i-1, i+1
#     if nums[j] < current and nums[k] > current:
#       beauty += 1
#       while j > 0 and nums[j] < current:
#         j -= 1
#       if j == 0:
#         while k < len(nums) and nums[k] > current:
#           k += 1
#         if k == len(nums):
#           beauty += 1
#   return beauty

#nums = [8,5,6,5,9,10]
nums = [x+1 for x in range(100000)]

print(sumOfBeauties(nums))
