# def numMatchingSubseq(s,words):
#   ret = 0
#   for word in words:
#     i, j = 0, 0
#     while i < len(word) and j < len(s):
#       if word[i] == s[j]:
#         i += 1
#       j += 1
#     if i == len(word):
#       ret += 1
  
#   return ret

# def numMatchingSubseq(s,words):
#   L = {}
#   for i in range(len(s)):
#     L[s[i]] = L.setdefault(s[i],[]) + [i]
  
#   ret = 0
#   for word in words:
#     current = 0
#     B = True
#     T = L.copy()
#     for i in word:
#         #Find the lowest index of said letter
#         #update current and update the dict
#         if i in T:
#           val_index = 0
#           while val_index < len(T[i]) and T[i][val_index] < current:
#             val_index += 1
#           if val_index == len(T[i]):
#             B = False
#             break
#           current = T[i][val_index] 
#           T[i] = T[i][val_index+1:]     
#         else:
#           B = False
#           break
#     if B:
#       ret += 1

#   return ret


def numMatchingSubseq(s,words):
  L = {}
  for word in words:
    L[word[0]] = L.setdefault(word[0],[]) + [word]
  
  count = 0
  for char in s:
    if char in L:
      temp = L[char]
      L[char] = []
      for st in temp:
        if len(st) == 1:
          count += 1
        else:
          L[st[1]] = L.setdefault(st[1],[]) + [st[1:]]

  return count
  





s = "abcde"
words = ["a","bb","acd","ace"]
s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]


print(numMatchingSubseq(s,words))