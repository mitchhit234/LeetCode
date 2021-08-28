#given the root of a BST, return the min
#difference between the values of any two different
#nodes in the tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rec(root):
  if root.left == None and root.right == None:
    return [root.val]
  elif root.left == None:
    return [root.val] + rec(root.right)
  elif root.right == None:
    return rec(root.left) + [root.val]
  
  return rec(root.left) + [root.val] + rec(root.right)

def minDiffInBST(root):
  l, mn = rec(root), 10**5 + 1

  for i in range(1,len(l)):
    mn = min(mn,l[i]-l[i-1])
  
  return mn 
  




i = TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(6))
print(minDiffInBST(i))
  


