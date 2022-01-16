import math

def minAreaFreeRect(points):
  if len(points) < 4:
    return 0

  #Find by picking two points then searching for
  #other points that exist if those 2 points were across
  #from each other in the square (center is the middle of the
  #line connecting the two points)

  squares = []
  while len(points) > 1:
    checker = points[0]
    for i in range(1,len(points)):
      a = check(checker,points[i],points)
      if a:
        squares.append(a)
    points = points[1:]

  #Iterate through all squares, find the minimum area
  mn = ((4*10**4)**2)+1
  for i in squares:
    mn = min(find_area(i),mn)

  return mn if mn < ((4*10**4)**2)+1 else 0


#Find if a and b form a valid rectangle
#as corner points opposite of each other
def check(a,b,P):
  #Find center point
  xc, yc = (a[0]+b[0])/2, (a[1]+b[1])/2
  xd, yd = (a[0]-b[0])/2, (a[1]-b[1])/2
  #Find radius of accompanying circle
  r = math.sqrt(xd**2 + yd**2)
  #Check all possible x y int values in the interval
  #for a possible vertex
  for i in range(int(xc-r+1),int(xc+r+1)):
    possible_y = r**2 - (i-xc)**2 - yc**2
    print(possible_y)

  n1 = [xc-yd, yc+xd]
  n2 = [xc+yd, yc-xd]


  if n1 in P and n2 in P:
    return [a,b,n1,n2]
  
  return False
  

#Point 1 and 2 should be opposite corners
#meaning lines [1,3] and [1,4] will multiply
#to give the area of the rectangle
def find_area(P):
    x1, y1 = abs(P[0][0] - P[2][0]), abs(P[0][1] - P[2][1])
    x2, y2 = abs(P[0][0] - P[3][0]), abs(P[0][1] - P[3][1])

    s1 = max(x1,y1)
    if x1 > 0 and y1 > 0:
      s1 = math.sqrt((x1**2) + (y1**2))

    s2 = max(x2,y2)
    if x1 > 0 and y1 > 0:
      s2 = math.sqrt((x2**2) + (y2**2))

    return s1*s2




r = [[1,2],[2,1],[1,0],[0,1]]
#r = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
print(minAreaFreeRect(r))