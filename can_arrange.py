class Solution:

  def canArrange(self,arr,k):

    freq = [0]*k
    for num in arr:
      freq[num%k] += 1


    i,j = 1,k-1
    while i < j:
      if freq[i] != freq[j]:
        return False
      i += 1
      j -= 1
    if i == j:
      if freq[i] % 2 != 0:
        return False

    return True



obj = Solution()
arr = [2,3,7,-9,4,4,7,3,2,10,8,15,2,1,-8,10,-5,10,-2,21,9,20,0,4,24,5,12,-10,8,9,18,13,-8,10,-4,-3,0,16,-4,8,14,15,-9,0,0,-6,11,-3,10,11,7,-1,-5,5,11,2,5,9,-2,8,9,-10,6,-2,7,8,3,0,-2,11]
k = 18
print(obj.canArrange(arr,k))