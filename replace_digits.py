class Solution:

  #ord gets you the int value of a char
  #chr gets you the char value of an int

  def replaceDigits(self,s):
    ret = ""
    for i in range(len(s)):
      if i % 2 == 0:
        ret += s[i]
      else:
        ret += chr(ord(s[i-1]) + int(s[i]))

    return ret



obj = Solution()
s = "a1c1e1"
print(obj.replaceDigits(s))