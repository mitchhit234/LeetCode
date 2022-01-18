import collections
# def numSplits(s):
#   l, r = 0, len(s)-1
#   while l <= r:
#     m = (l+r) // 2
#     val, ls, rs = check(s,m)
#     if val > 0:
#       l = m+1
#     elif val < 0:
#       r = m-1
#     else:
#       return calculate(s,ls,rs,m)

#   return l


# #Return 0 if equal
# #-1 if left has more, 1 if right has more
# def check(S,m):
#   ls, rs = set(), set()
#   for i in range(m):
#     ls.add(S[i])
#   for i in range(m,len(s)):
#     rs.add(S[i])
  
#   l, r = len(ls), len(rs)
#   if l > r:
#     return -1, ls, rs
#   elif l < r:
#     return 1, ls, rs
#   return 0, ls, rs


# def calculate(S,ls,rs,m):
#   count = 0
#   i = m-1
#   while S[i+1] in rs:
#     i -= 1
#     count += 1
#   i = m
#   while S[i] in ls:
#     i += 1
#     count += 1
#   return count
    
def numSplits(s):
  left_count = collections.Counter()
  right_count = collections.Counter(s)
  res = 0
  for c in s:
      left_count[c] += 1
      right_count[c] -= 1
      if right_count[c] == 0:
          del right_count[c]
      
      if len(left_count) == len(right_count):
          res += 1
          
  return res







s = "aacaba"
print(numSplits(s))