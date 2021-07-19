#given an array rectangles
#of each element = [l,w]
#return the number of rectangles
#that can create a square with a 
#side length of maxLen

def countGoodRectangles(rectangles):
  mx = 0
  for i in range(len(rectangles)):
    rectangles[i] = min(rectangles[i][0], rectangles[i][1])
    mx = max(mx, rectangles[i])
  
  return rectangles.count(mx)


r = [[5,8],[3,9],[5,12],[16,5]]
print(countGoodRectangles(r))