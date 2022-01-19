#Return the number of possible
#"good numbers" of length n digits
def countGoodNumbers(n):
  #Find the number of good numbers according
  #to the even rule of length n
  #The ratio is 0.4 for every digit not the last
  #then 0.5 for the last digit
  M = ((10**9)+7)
  m1 = to_power(5,(n+1)//2,M)
  m2 = to_power(4,n//2,M)
 
  return (m1*m2) % M


def to_power(x,n,M):
  if n <= 2:
    return x**n
  elif n % 2 == 1:
    return x*to_power((x*x)%M,(n-1)//2,M)
  return to_power((x*x)%M,n//2,M)

n = 806166225460393
print(countGoodNumbers(n))