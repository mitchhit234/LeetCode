def nearestValidPoint(x,y,points):

  current_value = 1 + 10**4
  current_index = -1

  for index, i in enumerate(points):
    man = current_value
    if i[0] == x:
      man = abs(y-i[1])
    elif i[1] == y:
      man = abs(x-i[0])

    if man < current_value:
        current_value = min(current_value,man)
        current_index = index


  return current_index



x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
print(nearestValidPoint(x,y,points))