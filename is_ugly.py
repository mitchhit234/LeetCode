#Given an integer n, return true
#if n is an ugly number
#Ugly numbers are numbers whose prime factors
#are limited to 2,3, and/or 5

def isUgly(n):
  if n <= 0:
    return False
  
  primes = [2,3,5]
  for i in primes:
    while n % i == 0:
      n //= i
  
  return n == 1


n = -2147483648
print(isUgly(n))





