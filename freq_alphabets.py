class Solution:

  def freqAlphabets(self,s):

    alph = []
    i = len(s)-1
    while i >= 0:
      if s[i] == '#':
        alph.append(s[i-2:i])
        i -= 2
      else:
        alph.append(s[i])
      i -= 1

    #a starts at 97, 1 + (96) = 97
    ret = ""
    for i in alph:
      ret += chr(int(i)+96)


    return ret[::-1]



obj = Solution()
s = "1326#"
print(obj.freqAlphabets(s))