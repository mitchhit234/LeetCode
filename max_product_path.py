class Solution:

    #Start at 0,0 can only move right or down
    #find the path to the end with the max non-negative product
    #return -1 if this is not possible
    def maxProductPath(self,grid):

      current = [0,0]
      while current != [len(grid),len(grid[0])]:
        


      return 0


obj = Solution()
grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
print(obj.maxProductPath(grid))