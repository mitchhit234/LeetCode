#given the root of a binary tree, determine
#if it is a mirror of itself

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
  return traverse(root,root)



def traverse(r1,r2):
  if r1 == None and r2 == None:
    return True
  elif r1 == None or r2 == None:
    return False
  else:
    return (r1.val == r2.val) and traverse(r1.left,r2.right) and traverse(r1.right,r2.left)





a = TreeNode(1,TreeNode(2,TreeNode(2)),TreeNode(2,TreeNode(2)))
b = isSymmetric(a)
print(b)