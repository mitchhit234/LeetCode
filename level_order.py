class Node:
  def __init__(self,val=None,children=None):
    self.val = val
    self.children = children

class Solution:
  
  def levelOrder(self,root):
    if root == None:
      return []

    queue = [root]
    ans = []
    while queue:
      level = []
      n = len(queue)
      for _ in range(n):
        cur = queue[0]
        queue = queue[1:]
        level.append(cur.val)
        if cur.children != None:
          for child in cur.children:
            queue.append(child)
      ans.append(level)
    return ans

obj = Solution()
root = Node(1,[Node(3,[Node(5),Node(6)]),Node(2),Node(4)])
print(obj.levelOrder(root))