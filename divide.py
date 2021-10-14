#Given two integers, return the 
#dividend / divider without using
#divide, multiply, or modulo

def divide(dividend,divisor):
  neg = False
  if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
    neg = True

  divisor, dividend = abs(divisor), abs(dividend)

  total = 0
  while dividend >= divisor:
    result = 1
    i = 0
    temp = divisor

    while dividend >= temp:
      temp <<= 1
      i = result
      result += result

    temp >>= 1
    result = i
    dividend -= temp
    total += result


  return max(-total,-2**31) if neg else min(total,2**31 - 1)


a = 2
b = 3
print(divide(a,b))
