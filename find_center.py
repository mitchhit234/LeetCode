#find the center of a star graph

def findCenter(edges):
  l = [edges[0][0],edges[0][1],edges[1][0],edges[1][1]]
  for i in l:
    if l.count(i) == 2:
      return i



edges = [[1,2],[2,3],[4,2]]
print(findCenter(edges))