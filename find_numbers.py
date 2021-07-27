#Given an array of nums, return how 
#many of the numbers contain an even number
#of digits

import math

def findNumbers(nums):
  ret = 0
  for i in nums:
    dig = 1
    while i >= 10:
      i //= 10
      dig += 1
    if dig % 2 == 0:
      ret += 1
  return ret

def findNumbers2(nums):
  ret = 0
  for i in nums:
    if int(math.log10(i)) % 2 == 1:
      ret += 1
  return ret

findNumbers2([1000])
