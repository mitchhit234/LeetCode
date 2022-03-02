class Solution:

  def isValid(self,s):
    base = "abc"
    needed = ""
    for i in s:
      if i == base[0]:
        needed = base[1:] + needed
      elif len(needed) > 0 and i == needed[0]:
        needed = needed[1:]
      else:
        return False

    if len(needed) == 0:
      return True
    return False



obj = Solution()
s = "aabcbc"
s = "abcabcababcc"
s = "abccba"
print(obj.isValid(s))