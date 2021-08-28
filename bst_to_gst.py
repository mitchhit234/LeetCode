#given the root of a BST, return it to a 
#greater tree such that every key of the 
#original key plus the sum of all keys 
#greater than the original key in BST

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  val = 0
  def bstToGst(self,root):
    if root.right: 
      self.bstToGst(root.right)
    root.val = self.val = self.val + root.val
    if root.left: 
      self.bstToGst(root.left)
    return root



i = TreeNode(4,TreeNode(1,TreeNode(0),TreeNode(2,None,TreeNode(3))),TreeNode(6,TreeNode(5),TreeNode(7,None,TreeNode(8))))
a = Solution()
b = a.bstToGst(i)
b = 0