#return the sum of the array of all
#possible substring sums from l position
#in that array to r position (sorted)


def rangeSum(nums,n,left,right):
  sum_list = []
  for i in range(n):
    prev_value = 0
    for j in range(i,n):
      sum_list.append(prev_value + nums[j])
      prev_value += nums[j]
      
  sum_list = sorted(sum_list)
  
  final_sum = 0
  for i in range(left-1,right):
    final_sum += sum_list[i]

  return final_sum % (10**9 + 7)


ex = [1,2,3,4]
n = 4
left = 1
right = 5
print(rangeSum(ex,n,left,right))
