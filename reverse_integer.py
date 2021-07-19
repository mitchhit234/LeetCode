#return integer x with its digits reversed
#def reverse(x):

INT_MAX_MIN = pow(2, 31)
def reverse(x):
  ret = 0
  multiplier = -1 if(x<0) else 1
  x *= multiplier
  while x != 0:
    temp = x%10
    ret = ret*10 + temp
    x //= 10
  return 0 if (ret < -INT_MAX_MIN or ret > INT_MAX_MIN - 1) else ret*multiplier

