#given tow integers a and b
#return any string s such that
#s has the length a+b and contains
#a letter a's and b letter b's
#neither the string aaa or bbb occurs

# def strWithout3a3b(a,b):
#   ret = ""
#   while a > 0 and b > 0:
#     if a > b:
#       ret += "aab"
#       a -= 2
#       b -= 1
#     elif a == b:
#       ret += "ba"
#       b -= 1
#       a -= 1
#     else:
#       ret += "bba"
#       b -= 2
#       a -= 1

#   if a > 0:
#     ret += "a"*a
#   if b > 0:
#     ret += "b"*b
  
#   return ret


def strWithout3a3b(a,b):
  x,y = "a", "b"
  ret = ""
  if b > a:
    temp = a
    a = b
    b = temp
    x,y = "b", "a"
  
  while a > 0:
    ret += x
    a -= 1
    if a > b:
      ret += x
      a -= 1
    if b > 0:
      ret += y
    b -= 1
  
  return ret




a = 4
b = 1
print(strWithout3a3b(a,b))