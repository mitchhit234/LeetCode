#given a string, return the number
#of segments in the string

def countSegments(s):
  if len(s) < 1:
    return 0
  
  seg = 0
  for i in range(1,len(s)):
    if s[i] == ' ' and s[i-1] != ' ':
      seg += 1
  
  if s[-1] != ' ':
    seg += 1
  
  return seg

  

s = "Hello, my name is John"
print(countSegments(s))