#Return num of possible unique
#BST's with n nodes

#n(1) = 1
#n(2) = 2
#n(3) = 5
def numTrees(n):
  if n <= 2:
    return n
  
  sm = 0
  for i in range(n):
    sm += numTrees(i) + numTrees(n-1-i)
    if i == 1 or n-1-i == 1:
      sm -= 1

  return sm


print(numTrees(6)) 
