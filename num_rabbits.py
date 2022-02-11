import math
class Solution:

  def numRabbits(self,answers):
    count = 0
    L = {}
    for i in answers:
      if i in L:
        L[i] += 1
      else:
        L[i] = 1

    for key in L:
      count += (key+1)*math.ceil(L[key]/(key+1))
      
    return count


obj = Solution()
answers = [1,1,2]
print(obj.numRabbits(answers))