#Find cascading sums
#detect the most common element
#subtract num walls minus occurrences
def leastBricks(wall):
  #Reorganize walls to show passible points
  sm = sum(wall[0])
  L = {}
  for i in range(len(wall)):
    L = add_to_dict(L,wall[i][0],1)
    for j in range(1,len(wall[i])):
      wall[i][j] += wall[i][j-1]
      L = add_to_dict(L,wall[i][j],1)
    #Last element will be the outer boundary for all
    if len(wall[i]) > 1:
      wall[i] = wall[i][:-1]

  mx_index, mx_value = 0, 0
  for key in L:
    if L[key] > mx_value:
      if key != sm:
        mx_index = key
        mx_value = L[key]
  
  return len(wall) - mx_value
  

def add_to_dict(D,k,v):
  if k in D:
    D[k] += v
  else:
    D[k] = v
  return D
  
  
  
  
  
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
#wall = [[1,1],[2],[1,1]]
print(leastBricks(wall))