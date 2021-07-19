#Given the roots of two binary trees,
#write a function to check if they are 
#identical or not


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p,q):
  if p == None and q == None:
    return True
  if p == None or q == None:
    return False
  if p.val != q.val:
    return False

  if isSameTree(p.left,q.left):
    return isSameTree(p.right,q.right)
  