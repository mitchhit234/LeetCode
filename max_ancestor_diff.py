#Given the root of a tree, find the max
#value v for which there exist different
#nodes a and b where v = |a.val - b.val|
#and a is an ancestor of b

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


leafs = []

def maxAncestorDiff(root):
  helper(root)
  l = abs(root.val - min(leafs))
  r = abs(root.val - max(leafs))
  return max(l,r)


def helper(root):
  if root.left == None or root.right == None:
    leafs.append(root.val)
  if root.left == None and root.right == None:
    return

  if root.left != None:
    helper(root.left)
  if root.right != None:
    helper(root.right)



#s = TreeNode(8,TreeNode(3,TreeNode(1),TreeNode(6,TreeNode(4),TreeNode(7))),TreeNode(10,None,TreeNode(14,TreeNode(13),None)))
s = TreeNode(1,None,TreeNode(2,None,TreeNode(0,TreeNode(3),None)))

print(maxAncestorDiff(s))
