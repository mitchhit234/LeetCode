#Given an integer, return the number
#of trailing zeros in n!

def trailingZeros(n):
  new = 1
  for i in range(2,n+1):
    new *= i
  
  count = 0
  st = str(new)[::-1]
  i = 0
  while st[i] == "0":
    i += 1
    count += 1

  return count


n = 100000
print(trailingZeros(n))