def primePalindrome(n):
  return 0



#Generate a list of prime numbers
#up to and including n
def generate_primes(n):
  #0 means unvisited, 1 means visited
  primes = []
  A = [0]*(n+1)
  A[0], A[1] = 1, 1
  for i in range(2,n+1):
    if A[i] == 0:
      primes.append(i)
      j = i
      while j < len(A):
        A[j] = 1
        j += i
  return primes



print(generate_primes(2*10**8))
