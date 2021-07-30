#given an input of unique integers arr, where each
#item is greater than one, return the number of possible
#binary trees we can make 

def numFactoredBinaryTrees(arr):
  mod = 10**9 + 7
  arr = sorted(arr)
  dp = {}
  for i in arr:
    dp[i] = 1

  for i in range(1,len(arr)):
    for j in range(i):
      if arr[i] == arr[j] * (arr[i]//arr[j]):
        if (arr[i]//arr[j]) in dp:
          dp[arr[i]] += dp[arr[j]] * dp[(arr[i]//arr[j])]

  ret = 0
  for i in arr:
    ret += dp[i] 

  return ret % mod



arr = [2,4,5,10]
print(numFactoredBinaryTrees(arr))