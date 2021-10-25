#Given a binary string, return the
#min number of bit flips
#to make the string entirely alternating

def minFlips(s):
  window = len(s)
  s += s
  s1, s2 = "", ""
  for i in range(len(s)):
    s1 += str((i+1)%2)
    s2 += str(i%2)

  s1c, s2c = 0, 0
  for i in range(window):
    if s[i] != s1[i]: s1c += 1
    if s[i] != s2[i]: s2c += 1
  
  mn = min(s1c,s2c)

  for i in range(window,len(s)):
    if s[i] != s1[i]: s1c += 1
    if s[i] != s2[i]: s2c += 1

    if s[i-window] != s1[i-window]: s1c -= 1
    if s[i-window] != s2[i-window]: s2c -= 1

    mn = min(s1c,s2c,mn)

  return mn

    


s = "01001001101"
print(minFlips(s))


