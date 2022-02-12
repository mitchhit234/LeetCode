class Solution:

  def arrayRankTransform(self,arr):

    if len(arr) > 0:
      srt = sorted(arr)
      L = {}
      rank = 1
      L[srt[0]] = rank
      for i in range(1,len(srt)):
        if srt[i-1] != srt[i]:
          rank += 1
        L[srt[i]] = rank

      for i in range(len(arr)):
        arr[i] = L[arr[i]]

    return arr




obj = Solution()
arr = [37,12,28,9,100,56,80,5,12]
print(obj.arrayRankTransform(arr))