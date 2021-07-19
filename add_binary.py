#Given two binary strings a and
#b, return their sum as a binary string

def addBinary(a,b):
  base_10 = int(a) + int(b)

  if base_10 == 0:
    return "0"
  
  ret = ""
  while base_10 != 0:
    digit = base_10 % 10
    if digit > 1:
      base_10 += (digit//2)*10
      digit = digit % 2
    ret += str(digit)
    base_10 //= 10
  
  return ret[::-1]
  



print(addBinary("1111111111","111111111"))