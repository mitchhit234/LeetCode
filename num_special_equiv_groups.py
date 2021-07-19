#given an array of strings called words,
#return the number of special equivalent
#strings from the group

#input integer x > 1
#does not find including x
def find_primes_to_x(x):
  #0 means unchecked, 1 means prime, -1 means not prime
  track = [0] * (x+1)
  #0 and 1 are not prime, 2 is prime
  track[0] = -1
  track[1] = -1

  i = 2
  while i < len(track)-1:
    if track[i] == 0:
      track[i] = 1
      for j in range(i*i,len(track),i):
        track[j] = -1
    i += 1

  primes = []
  for index, val in enumerate(track):
    if val == 1:
      primes.append(index)

  return primes


def numSpecialEquivGroups(words):
  primes = find_primes_to_x(102)
  prime_index = 0
  lookup = dict()

  new = []
  for word in words:
    word_even = ""
    word_odd = ""
    for i in range(len(word)):
      if word[i] not in lookup.keys():
        lookup[word[i]] = primes[prime_index]
        prime_index += 1
      if i % 2 == 0:
        word_even += word[i]
      else:
        word_odd += word[i]
    c, d = 1, 1
    for j in word_even:
      c *= lookup[j]
    for k in word_odd:
      d *= lookup[k]
    if [c,d] not in new:
      new.append([c,d])
  
  return len(new)



words = ["abc","acb","bac","bca","cab","cba"]


print(numSpecialEquivGroups(words))