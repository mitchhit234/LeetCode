#Given a string s, return the digits represented
#in ascending order

def gcd(a,b):
  if a % b == 0:
    return a/b
  else:
    return gcd(b,a%b)

#Get the primes up to n
def getPrimes(n):
  L = [0] * n
  L[0] = L[1] = -1
  for i in range(2,n):
    if L[i] == 0:
      L[i] = 1
      index = i+i
      while index < n:
        L[index] = -1
        index += i
  
  return [i for i in range(n) if L[i] == 1]



def originalDigits(s):
  letters = ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]
  numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
  
  #Assign letters to prime numbers
  x = getPrimes(50)
  lookup = {}
  for i in range(len(letters)):
    lookup[letters[i]] = x[i]

  #Assign number strings to prime factorizations
  number_values = []
  for i in numbers:
    cur = 1
    for j in i:
      cur *= lookup[j]
    number_values.append(cur)

  #Calculate value of input string
  st = 1
  for i in s:
    st *= lookup[i]

  #Find then numbers which are factors of the string
  found = []
  number_values.sort(reverse=True)
  for i in range(len(number_values)):
    j = 1
    #Find how many occurences of said number exist
    while st % (number_values[i]**j) == 0:
      j += 1
      found.append(str(i))
    st /= (number_values[i]**(j-1))




  
  return found


s = "zeroonetwothreefourfivesixseveneightnine"
print(originalDigits(s))
