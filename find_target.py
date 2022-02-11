# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def findTarget(self, root, k):
        L = {}
        for val in self.traverse(root):
          if val in L:
            L[val] += 1
          else:
            L[val] = 1
        
        for key in L:
          if (k-key) in L:
            if not ((k-key) == key and L[key] == 1):
              return True

        return False

    def traverse(self,root):
      if not root.left and not root.right:
        return [root.val]
      a, b = [], []
      if root.right:
        a = self.traverse(root.right)
      if root.left:
        b = self.traverse(root.left)

      return [root.val] + a + b





obj = Solution()
k = 9
root = TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(6,None,TreeNode(7)))

print(obj.findTarget(root,k))