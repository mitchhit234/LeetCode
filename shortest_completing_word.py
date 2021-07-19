#Given a string licensePlate and an
#array of words called words, find the 
#shortest world in words that contains
#all the letters in liscensePlate
#IGNORE NUMBERS AND SPACES
#IGNORE UPPER/LOWER CASE

from string import ascii_lowercase

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






def shortestCompletingWord(licensePlate,words):
  i = 0
  while i < len(licensePlate):
    if licensePlate[i].isalpha():
      licensePlate = licensePlate[:i] + licensePlate[i].lower() + licensePlate[i+1:]
      i += 1
    else:
      licensePlate = licensePlate[:i] + licensePlate[i+1:]

  primes = find_primes_to_x(102)

  lookup = dict()
  for i in range(len(ascii_lowercase)):
    lookup[ascii_lowercase[i]] = primes[i]

  license_product = 1
  for i in licensePlate:
    license_product *= lookup[i]

  match = "!"
  for word in words:
    product = 1
    for char in word:
      product *= lookup[char]
    
    if product % license_product == 0:
      if len(word) < len(match) or match == "!":
        match = word
      if len(match) == len(licensePlate):
        return match

  return match

  


  




licensePlate = "iMSlpe4"
words = ["claim","consumer","student","camera","public","never","wonder","simple","thought","use"]

print(shortestCompletingWord(licensePlate,words))



