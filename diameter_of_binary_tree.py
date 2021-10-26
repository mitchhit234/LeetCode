#given the root of a binary tree return
#the length of the diameter of the tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


cur = 0
def diameterOfBinaryTree(root):
  depth(root)
  return count


def depth(p):
  if not p:
    return 0

  left, right = depth(p.left), depth(p.right)
  cur = max(cur,let+right)
  return 1 + max(left,right)




r = TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(12)),TreeNode(5)),TreeNode(3))

depth(r)
print(cur)
