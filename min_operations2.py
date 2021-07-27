#operations being addition by
#one and multiplication by two,
#return the min number of operations
#to transform an array of 0's to nums

def minOperations(nums):
  l = [bin(a).count('1') for a in nums]
  return sum(l) + len(bin(max(nums)))-2-1
  


print(minOperations([4,2,5]))

#0100
#0010
#0101
