#Given the root of a binary tree, 
#return the in order traversal of its
#nodes values


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
  if root == None:
    return None

  if root.left == None and root.right == None:
    return [root.val]

  if root.right == None:
    return inorderTraversal(root.left) + [root.val]
  elif root.left == None:
    return [root.val] + inorderTraversal(root.right)
  else:
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


a = inorderTraversal(TreeNode(3,TreeNode(1),TreeNode(2)))
b = 0