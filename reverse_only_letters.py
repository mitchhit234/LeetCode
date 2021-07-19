#Given a string s, return the 
#reversed string where all characters
#that are not letters stay in the same place

def isLetter(c):
  if c > 64 and c < 123:
    if not 90 < c < 97:
      return True
  return False

def reverseOnlyLetters(s):
  alph = ""
  for i in s:
    if isLetter(ord(i)):
      alph = alph + i
  alph = alph[::-1]
  
  ret = ""
  for i in range(len(s)):
    if isLetter(ord(s[i])):
      ret += alph[0]
      alph = alph[1:]
    else:
      ret += s[i]

  return ret


a = "a-bC-dEf-ghIj"
print(reverseOnlyLetters(a))