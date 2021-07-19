#Given a 2d array boxTypes and integer truck size
#return the maximum number of boxes that
#can be put on the truck

def maximumUnits(boxTypes,truckSize):

  m = max(boxTypes,key= lambda x: x[1])[1]

  search_desc = [0] * (m+1)
  for i in boxTypes:
    search_desc[i[1]] += i[0]
  
  ret = 0

  for i in range(len(search_desc)-1,-1,-1):
    if search_desc[i] != 0:
      while search_desc[i] > 0:
        ret += i
        search_desc[i] -= 1
        truckSize -= 1
        if truckSize < 1:
          return ret
  
  return ret









boxTypes = [[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]]
truckSize = 13
print(maximumUnits(boxTypes,truckSize))
