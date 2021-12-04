#Given two anagrams, return the smallest k for which
#s1 and s2 and k similar
def kSimilarity(s1,s2):
  status = []
  for i,j in zip(s1,s2):
    if i == j:
      status.append(1)
    else:
      status.append(0)

  return status







s1 = "aabc"
s2 = "abca"
print(kSimilarity(s1,s2))
