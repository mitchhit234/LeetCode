#Given a non negative integer x,
#compute the square root of x
#truncated to an integer

def mySqrt(x):
  lower, upper = 0, x
  while True:
    mid = lower + (upper-lower)//2
    if mid*mid <= x < (mid+1)*(mid+1):
      return mid
    elif x < mid*mid:
      upper = mid-1
    else:
      lower = mid+1






print(mySqrt(500))