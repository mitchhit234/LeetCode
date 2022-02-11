#given a string s and an integer k,
#make k duplicate removals until no
#more can be made

class Solution:

    def removeDuplicates(self,s,k):

      stack = [['#',0]]
      for i in s:
        if stack[-1][0] == i:
          stack[-1][1] += 1
          if stack[-1][1] == k:
            stack.pop()

        else:
          stack.append([i,1])

      return "".join([a*b for a, b in stack])



obj = Solution()
s = "pbbcggttciiippooaais"
k = 2
print(obj.removeDuplicates(s,k))