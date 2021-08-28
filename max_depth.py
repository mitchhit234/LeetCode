#given a n-ary tree, find its
#maximum depth

class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children


def maxDepth(root):
  if root == None:
    return 0
  elif root.children == None:
    return 1
  mx = 0
  for i in root.children:
    mx = max(mx,maxDepth(i)) 
  return mx + 1
  


n = Node(1,[Node(3,[Node(5),Node(6)]),Node(2),Node(4)])
print(maxDepth(n))