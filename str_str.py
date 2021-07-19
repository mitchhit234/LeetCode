#return the index of the beggining of the
#substring needle in the string haystack

def strStr(haystack, needle):
  if not needle:
    return 0
  if not haystack:
    return -1
  if needle == haystack:
    return 0
  
  l = len(needle)
  for index in range(len(haystack)-len(needle)+1):
    if haystack[index] == needle[0]:
      if haystack[index:index+l] == needle:
        return index
  return -1

print(strStr("a","a"))