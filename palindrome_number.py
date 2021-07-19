#Given an integer x
#return true if palindrome, false if not


def isPalindrome(x):

  if x < 0 or (x % 10 == 0 and x != 0):
    return False

  pal = 0
  while pal < x:
    temp = x%10
    pal = pal*10 + temp
    x //= 10

  if pal == x or pal//10 == x:
    return True
  return False

  

print(isPalindrome(1000001))
