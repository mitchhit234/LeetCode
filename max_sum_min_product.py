#Get the min value of the array
#multiplied by the array's sum
#maximized by creating subarrays
def maxSumMinProduct(nums):
  prefix = [nums[0]]
  for i in range(1,len(nums)):
    prefix.append(nums[i]+prefix[i-1])

  mx = 0
  for i in range(len(nums)):
    l, r = get_lr_sum(nums,i)
    sm = prefix[r]
    if l >= 0:
      sm -= prefix[l]
    mx = max(mx,nums[i]*sm)

  return mx

def get_lr_sum(N,i):
  l, r = i-1, i+1
  while l >= 0 and N[l] >= N[i]:
    l -= 1
  while r < len(N) and N[r] >= N[i]:
    r += 1
  
  return l, r-1

nums = [1,2,3,2]
nums = [2,3,3,1,2]
#nums = [3,3,2,2,3,1,1,4,1,3]
print(maxSumMinProduct(nums))



