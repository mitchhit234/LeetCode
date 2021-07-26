#given a string s, return the 
#number of unique palindromes
#of length three that are a
#subsequence of s

def get_primes(n):

  ref = [0] * (n+1)
  ref[0], ref[1] = -1, -1

  i = 2
  while i < n:
    if ref[i] == 0:
      ref[i] = 1
      j = 2*i
      while j < n:
        ref[j] = -1
        j += i
    i += 1
  
  ret = []
  for index, i in enumerate(ref):
    if i == 1:
      ret.append(index)

  return ret
        





def countPalindromicSubsequence(s):
  letters = "abcdefghijklmnopqrstuvwxyz"
  lookup = dict()
  for i in letters:
    lookup[i] = [-1,-1]

  for i in range(len(s)):
    if lookup[s[i]][0] != -1:
      lookup[s[i]][1] = i
    else:
      lookup[s[i]][0] = i

  count = 0
  for i in range(len(letters)):
    l = lookup[letters[i]]
    if l[1] != -1:
      unique = []
      for j in range(l[0]+1,l[1]):
        if s[j] not in unique:
          unique.append(s[j])
      count += len(unique)

  
  return count
  




s = "aabca"
print(countPalindromicSubsequence(s))