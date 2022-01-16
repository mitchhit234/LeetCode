import math

def minAreaFreeRect(points):
  if len(points) < 4:
    return 0

  #Get all possible squares 
  #distinct groups of 4 vertices
  poss = sub(points,4)

  for i in poss:
    check(i)


  return 0



def sub(S,k):
  if k == 0:
    return []
  if k <= 1:
    return [S]

  ret = []
  for i in range(0,len(S)-(k-1)):
    for tail in sub(S[i+1:],k-1):
      ret.append([S[i]] + tail)
  return ret


def check(P):
  #Check two random sides, makes sure the other two
  #sides have the same connecting line length
  if line_between(P[0][0],P[0][1],P[1][0],P[1][1]) == line_between(P[2][0],P[2][1],P[3][0],P[3][1]) :
    print(P)


def line_between(x1,y1,x2,y2):
  if x1 == x2:
    return abs(y1-y2)
  if y1 == y2:
    return abs(x1-x2)
  
  return math.sqrt((x2-x1)**2 + (y2-y1)**2)



P = [[0,1],[2,1],[1,1],[1,0],[2,0]]
print(minAreaFreeRect(P))
