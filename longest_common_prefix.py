#return the largest common prefix among
#a list of strings

def longestCommonPrefix(strs):
  if len(strs) == 0:
    return ""
  min_index = 0
  min_length = 201
  for index, value in enumerate(strs):
    if len(value) < min_length:
      min_length = len(value)
      min_index = index
  
  to_compare = strs[min_index]
  prefix=""
  for index, value in enumerate(to_compare):
    for j in strs:
      if j[index] != value:
        return prefix
    prefix += value

  return prefix




strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))