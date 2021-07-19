#Given an array of integers arr, find a pattern
#of length m that is repeated k or more times

def containsPattern(arr,m,k):
  for i in range(len(arr)-m):
    x = 1
    while arr[i:i+m] == arr[i+(x*m):i+m+(x*m)] and x < k:
      x += 1
    if x == k:
      return True

  return False



arr = [1,2,4,4,4,4]
m = 2
k = 2
print(containsPattern(arr,m,k))