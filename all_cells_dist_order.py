#given a matrix rows and cols
#return the coordiantes of all cells
#sorted by their distance from [rCenter,cCenter]

#distance = |r1 - r2| + |c1 - c2|

def allCellsDistOrder(rows,cols,rCenter,cCenter):
  lookup = dict()

  for row in range(rows):
    for col in range(cols):
      key = abs(rCenter-row)+abs(cCenter-col)
      lookup[key] = lookup.get(key, []) + [[row,col]]

  ret = []
  for i in range(len(lookup.keys())):
    for j in lookup[i]:
      ret.append(j)

  return ret



rows = 2
cols = 3
rCenter = 1
cCenter = 2
print(allCellsDistOrder(rows, cols, rCenter, cCenter))