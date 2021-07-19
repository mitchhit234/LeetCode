#Return a string that is the lowercase
#version of s

def toLowerCase(s):
  for i in range(len(s)):
    if 64 < ord(s[i]) < 91:
      s = s[:i] + chr(ord(s[i])+32) + s[i+1:]
  return s

s = "al&phaBET"
print(toLowerCase(s))