
#Given an array nums of integers,
#obtain a subsequence of the array
#whose sum of elements is greater than
#the sum of the non included elements

def minSubsequence(nums):
  search, total = [0]*101, 0
  for i in nums:
    total += i
    search[i] += 1
  total /= 2
  
  count, ret  = 0, []
  for i in range(len(search)-1,-1,-1):
    while search[i] != 0:
      count += i
      ret.append(i)
      search[i] -= 1
      if count > total:
        return ret

  return ret

      
      

      

n = [4,3,10,9,8]
print(minSubsequence(n))