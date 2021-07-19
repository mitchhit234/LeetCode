#given an integer, an array
#of nums of length n+1 is generated 
#the following way

# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

def getMaximumGenerated(n):
  if n <= 1:
    return n

  ret = [0,1]

  for i in range(2,n+1):
    if i % 2 == 0:
      ret.append(ret[i//2])
    else:
      ret.append(ret[i//2]+ret[(i//2)+1])

  return max(ret)



print(getMaximumGenerated(7))