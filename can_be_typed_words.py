#return number of words in the text that can be written
def canBeTypedWords(text,brokenLetters):
  text = text.split(" ")
  count = len(text)
  primes = prime_generate(103)
  alp = "abcdefghijklmnopqrstuvwxyz"
  lookup = {}
  for i in range(len(primes)):
    lookup[alp[i]] = primes[i]

  for i in text:
    value = 1
    for j in i:
      value *= lookup[j]

    for x in brokenLetters:
      if value % lookup[x] == 0:
        count -= 1
        break


  # for i in text:
  #   for j in brokenLetters:
  #     if j in i:
  #       count -= 1
  #       break

  return count


def prime_generate(N):
  #-1 represents unvisited, 0 prime, 1 not prime
  A = [-1]*N
  A[0] = 1
  for i in range(2,N):
    index = i-1
    if A[index] == -1:
      A[index] = 0
      val = i
      while index < N-val:
        index += val
        A[index] = 1

  ret = []
  for i in range(len(A)):
    if A[i] == 0:
      ret.append(i+1)

  return 





text = "hello world"
brokenLetters = "ad"
print(canBeTypedWords(text,brokenLetters))
print(len(prime_generate(103)))
