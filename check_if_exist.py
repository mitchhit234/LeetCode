class Solution:

  def checkIfExist(self,arr):

    L = {}
    for i in arr:
      L[i] = True

    for key in L:
      if key*2 in L:
        if key != 0:
          return True

    return False



obj = Solution()
arr = [-2,0,10,-19,4,6,-8]
print(obj.checkIfExist(arr))