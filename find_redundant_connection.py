# def findRedundantConnection(edges):
#   #Get the counts of each edge in the graph
#   L, X = {}, {}
#   for i in edges:
#     L[i[0]] = L.setdefault(i[0],0) + 1
#     L[i[1]] = L.setdefault(i[1],0) + 1
#     X[i[0]] = X.setdefault(i[0],[]) + [i[1]]
#     X[i[1]] = X.setdefault(i[1],[]) + [i[0]]

#   a = 0
#   #Search for edges from back to front
#   #Skip edge if it contains a node that
#   #only has one edge, else return it

#   #Make sure the other edges of attached points 
#   #have at least one edge outside of the one with our points
#   for i in range(len(edges)-1,-1,-1):
#     x, y = edges[i][0], edges[i][1]
#     if L[x] > 1 and L[y] > 1:
#       f1, f2 = True, True
#       for j in X[x]:
#         if L[j] <= 1:
#           f1 = False
#       for k in X[y]:
#         if L[k] <= 1:
#           f2 = False
      
#       if f1 or f2:
#         return edges[i]

#   return False


def findRedundantConnection(edges):
  sets = []
  for edge in edges:
    x, y = edge[0], edge[1]
    added_to = []
    found = False
    for j in range(len(sets)):
      #If both are in a set, theres a cycle
      if x in sets[j] and y in sets[j]:
        return edge
      #If one is in a set, add the other, keep checking
      if x in sets[j]:
        sets[j].append(y)
        added_to.append(j)
        found = True
      elif y in sets[j]:
        sets[j].append(x)
        added_to.append(j)
        found = True
      #If none are in the set, move on
    
    if not found:
      sets.append([x,y])

    if len(added_to) == 2:
      s1, s2 = sets[added_to[0]], sets[added_to[1]]
      sets.remove(s1)
      sets.remove(s2)
      temp = set(s1+s2)
      sets.append(list(temp))

    
    #If not in any sets, 


e = [[1,2],[2,3],[3,4],[1,4],[1,5]]
e = [[1,2],[1,3],[2,3]]
# e = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
e = [[1,5],[3,4],[3,5],[4,5],[2,4]]
print(findRedundantConnection(e))
