#guven n points on a 2d plane, return
#the widest vertical areas (in terms of width) between two
#points such that no points are inside the area

def maxWidthOfVerticalArea(points):
  diff = 0
  points = sorted(points, key= lambda x: x[0])
  for i in range(1,len(points)):
    diff = max(diff,points[i][0]-points[i-1][0])
  return diff


p = [[8,7],[9,9],[7,4],[9,7]]
print(maxWidthOfVerticalArea(p))

