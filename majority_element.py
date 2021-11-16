def majorityElement(nums):
  count = 0
  canidate = 0

  for i in nums:
    if count == 0:
      canidate = i
    if i == canidate:
      count += 1
    else:
      count -= 1
    
  return canidate

s = [2,2,1,1,1,2,2]
print(majorityElement(s))