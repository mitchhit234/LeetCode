#Find cells in the matrix
#where rainwater can flow to 
#both the pacific and atlantic ocean

def pacificAtlantic(heights):
  m = len(heights)
  n = len(heights[0])
  
  pacific = [[1 if x == 0 or y == 0 else 0 for x in range(n)] for y in range(m)]
  atlantic = [[1 if x == m-1 or y == n-1 else 0 for x in range(n)] for y in range(m)]
  visited = [[1 if x == m-1 or x == 0 or y == 0 or y == n-1 else 0 for x in range(n)] for y in range(m)]


  for i in range(1,m-1):
    for j in range(1,n-1):
      if visited[i][j] == 0:
        #check north neighbor
        atlantic, pacific = check(i,j,i-1,j,visited,pacific,atlantic)       
        #check east neighbor
        atlantic, pacific = check(i,j,i,j+1,visited,pacific,atlantic)   
        #check south neighbor
        atlantic, pacific = check(i,j,i+1,j,visited,pacific,atlantic)   
        #check west neighbor
        atlantic, pacific = check(i,j,i,j-1,visited,pacific,atlantic)  
        
        visited[i][j] = 1 
  
  ret = []
  for i in range(len(pacific)):
    for j in range(len(pacific[0])):
      if pacific[i][j] == 1 and atlantic[i][j] == 1:
        ret.append([i,j])

  return ret


def check(i,j,ni,nj,visited,pacific,atlantic):
  if heights[i][j] >= heights[ni][nj]:
    if atlantic[ni][nj] == 1:
      atlantic[i][j] = 1
    if pacific[ni][nj] == 1:
      pacific[i][j] = 1
  return atlantic,pacific





heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))