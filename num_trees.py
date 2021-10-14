#Return num of possible unique
#BST's with n nodes

#n(1) = 1
#n(2) = 2
#n(3) = 5
def numTrees(n):
  if n <= 2:
    return n
  
  sm = 0
  for i in range(n-1):
    sm += numTrees(i) + numTrees()


print(numTrees(3)) 
