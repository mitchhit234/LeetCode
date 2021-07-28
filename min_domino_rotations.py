#tops and bottoms represent the top and
#bottom half of ith domino
#we can rotate so top and bottom swap values for i
#return the min number of rotations such that all
#the values in top or the bottom are the same
#return -1 if not possible

def minDominoRotations(tops,bottoms):
  mx = -1
  for i in range(1,7):
    store = [0,0,0]
    for j in range(len(tops)):
      if tops[j] == i and bottoms[j] == i:
        store[2] += 1
      if tops[j] == i:
        store[0] += 1
      if bottoms[j] == i:
        store[1] += 1 
    if store[0] + store[1] - store[2] == len(tops):
      mx = max((len(tops)-max(store[0],store[1])),mx)
  
  return mx
  
      
      





tops = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
print(minDominoRotations(tops,bottoms))