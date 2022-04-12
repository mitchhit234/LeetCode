class Solution:
    def shortestBridge(self, grid):
      dirs = [[-1,0],[1,0],[0,-1],[0,1]]
      found = False
      for i in range(len(grid)):
        for j in range(len(grid[i])):
          if grid[i][j] == 1:
            grid, stack = self.dfs(grid,i,j,[])
            found = True
            break
        if found:
          break

      count = -1
      while True:
        count += 1
        next_step = []
        while len(stack) > 0:
          x, y = stack[0][0], stack[0][1]
          stack = stack[1:]  
          for d in dirs:
            i, j = x + d[0], y + d[1]
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]): 
              if grid[i][j] == 1:
                return count
              elif grid[i][j] == 0:
                grid[i][j] = -1
                next_step.append([i,j])    
        stack = next_step
            
      return

    def dfs(self,grid,x,y,stack):
      stack.append([x,y])
      grid[x][y] = 2
      dirs = [[-1,0],[1,0],[0,-1],[0,1]]
      for direction in dirs:
        i, j = direction[0], direction[1]
        if 0 <= x+i < len(grid) and 0 <= y+j < len(grid[0]) and grid[x+i][y+j] == 1:
          grid, stack = self.dfs(grid,x+i,y+j,stack)
      return grid, stack




obj = Solution()
grid = [[0,1],[1,0]]
#grid = [[0,1,0],[0,0,0],[0,0,1]]
#grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(obj.shortestBridge(grid))