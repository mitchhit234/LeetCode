#Given a string, return the shortest palindrome
#possible by adding any # of chars in front of it
def shortestPalindrome(s):
  if len(s) < 2:
    return s

  length = KMP(s)
  to_add = s[length+1:]
  s = to_add[::-1] + s
  return s

  
  # a,b = 0, len(s)-1
  # while a < b:
  #   if s[a] == s[b]:
  #     a += 1
  #     b -= 1
  #   else:
  #     s = s[:a] + s[b] + s[a:]
  #     a += 1
  
  return s


def KMP(s):
  table = [0]*len(s)
  i, j = 0, 1
  while j < len(s):
    if s[i] == s[j]:
      table[j] = table[j-1] + 1
      i += 1
    else:
      i = 0
      if s[i] == s[j]:
        table[j] = 1
      else:
        table[j] = 0
      
    j += 1
  
  return table[-1]




s = "abcd"
s = "aacecaaa"
print(KMP(s))
print(shortestPalindrome(s))