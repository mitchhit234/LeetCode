#given an array of integers nums and an integer target
#return the number of non empty subsequences of nums
#such that the sum of min+max <= target modulo 10^9 + 7

def numSubseq(nums,target):
  ret = 0
  nums = sorted(nums)
  i, j = 0, len(nums)-1
  mod = ((10**9)+ 7)
  while i <= j:
    if nums[i] + nums[j] <= target:
      ret += (2**(j-i)) % mod
      i += 1
    else:
      j -= 1

  return ret % mod






d = [14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14]
target = 22

print(numSubseq(d,target))