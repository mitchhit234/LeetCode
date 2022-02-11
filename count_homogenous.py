#given a string s, return the number
#of homogenous substrings of s

class Solution:

  def countHomogenous(self,s):

    #Count up the contiguous same letter
    #subsequences and their length
    L = {}
    current = ""
    for i in s:
      if i == current:
        L[i][-1] += 1
      elif i in L:
        L[i].append(1)
      else:
        L[i] = [1]
      current = i

    #1 -> 1, 2 -> 3, 3 -> 6, 4 -> 10
    #Summation of the numbers up to n
    ret = 0
    for key in L:
      for val in L[key]:
        ret += self.sum_to_n(val)

    return ret % (10**(9) + 7)


  def sum_to_n(self,n):
    return int((n/2)*(1+n))

obj = Solution()
s = "zzzzz"
print(obj.countHomogenous(s))
