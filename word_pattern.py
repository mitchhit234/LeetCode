#given a string pattern and a 
#string s, find if s follows
#the same pattern

def wordPattern(pattern,s):
  s = s.split(' ')
  if len(pattern) == len(s):
    lookup = dict()
    for i in range(len(pattern)):
      if pattern[i] not in lookup.keys():
        lookup[pattern[i]] = s[i]
      if lookup[pattern[i]] != s[i]:
        return False
      if len(set(lookup.values())) != len(lookup.keys()):
        return False   
  else:
    return False

  return True


p = "abba"
s = "dog cat cat dog"
print(wordPattern(p,s))