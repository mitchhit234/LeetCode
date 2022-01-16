class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root,k):
  L = recur(root)
  return L[k-1]

def recur(root):
  if root.left == None and root.right == None:
    return [root.val]
  
  if root.left == None:
    return [root.val] + recur(root.right)
  if root.right == None:
    return recur(root.left) + [root.val]

  r = recur(root.right)
  l = recur(root.left)

  return l + [root.val] + r

r = TreeNode(2,TreeNode(1),None)
#r = TreeNode(3,TreeNode(1,None,TreeNode(2)),TreeNode(4))
print(kthSmallest(r,1))





        