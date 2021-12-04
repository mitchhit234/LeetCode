def to_base_x(n,x):
  n = int(n)
  s = ""
  while n:
    s = str(n % x) + s
    n //= x
  return s  



def solution(n,b):

  visited = []
  visited.append(n)
  
  y = ''.join(sorted(n, key=lambda a: float(a)))
  x = y[::-1]
  x = to_base_x(int(x),b)
  y = to_base_x(int(y),b)
  z = x - y
  
  print(x)
  print(y)
  print(z)


a = "1211"
b = 10
solution(a,b)

  

