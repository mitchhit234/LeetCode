#given an integer n, reorder the digits
#in any order such that the leading digit
#is not zero
#return true if and only if we can do this
#so that the resulting number is a power of 2

from math import log

# def reorderedPowerOf2(n):
#   if log(n,2) % 1 == 0:
#     return True

#   st = str(n)
#   l = [char for char in st]

#   perm(l,0)


# def list_to_num(L):
#   if L[0] == '0': 
#     return -1
#   base, num = 1, 0
#   for i in range(len(L)-1,-1,-1):
#     num += int(L[i]) * base
#     base *= 10
#   return num

# def perm(s,start):
#   if start == len(s):
#     num = list_to_num(s)
#     if num > 0:
#       if log(list_to_num(s),2) % 1 == 0:
#         return True
  
#   for i in range(start,len(s)):
#     s[start], s[i] = s[i], s[start]
#     perm(s,start+1)
#     s[i], s[start] = s[start], s[i]

def reorderedPowerOf2(n):
  og = str(n)
  for i in range(int(log(10**9,2))+1):
    check = str(2**i)
    if len(check) > len(og):
      return False
    elif len(check) == len(og):
      ret = True
      for i in check:
        if check.count(i) != og.count(i):
          ret = False
      if ret:
        return ret
  
  return False





print(reorderedPowerOf2(46))








