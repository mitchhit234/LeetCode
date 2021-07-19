#Given a grid of integers, return how many
#3x3 magic square subgribs there are

def numMagicSquaresInside(grid):
  ret = 0
  for i in range(len(grid)-2):
    for j in range(len(grid[i])-2):
      if starting_point(i,j,grid):
        ret += 1
      
  return ret




def starting_point(x,y,grid):
  running_list = []
  for i in range(x,x+3):
    for j in range(y,y+3):
      if not 0 < grid[i][j] < 10 or grid[i][j] in running_list:
        return False
      running_list.append(grid[i][j])

  i, j = 0, 8
  while i <= j:
    if running_list[i] + running_list[j] != 10:
      return False
    i += 1
    j -= 1

  for i in range(0,len(running_list),3):
    if running_list[i] + running_list[i+1] + running_list[i+2] != 15:
      return False
  
  for j in range(0,3):
    if running_list[j] + running_list[j+3] + running_list[j+6] != 15:
      return False

  return True
        









g = [[2,7,6],[1,5,9],[4,3,8]]
print(numMagicSquaresInside(g))