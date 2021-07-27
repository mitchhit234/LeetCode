#Given an integer array nums,
#return the min number of moves
#required to make all array elements equal

def minMoves(nums):
  ret, m = 0, min(nums)
  for i in nums:
    ret += (i-m)
  return ret


n = [1,2,3]
print(minMoves(n))




