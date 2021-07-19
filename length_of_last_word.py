#Given a string s, return the length of
#the last word in the string
#words seperated by spaces

def lengthOfLastWord(s):
  s = s.rstrip()[::-1]
  
  a = True
  l = 0
  while a and l < len(s):
    if s[l] == " ":
      a = False
    else:
      l += 1
  
  return l

  


print(lengthOfLastWord("a "))