class Solution:
  def circularArrayLoop(self, nums) -> bool:
    n = len(nums)
    indices = dict.fromkeys([x for x in range(len(nums))])
    while len(indices) > 0:
      index = list(indices.keys())[0]
      visited = []
      while index not in visited:
        visited.append(index)
        if index in indices:
          del indices[index]
        else:
          break
        index = (index + nums[index]) % n

      start = visited.index(index)
      ret = self.sign_check(nums,visited[start:])

      if ret == True:
        break
    
    return ret
 

  def sign_check(self,L,ids):
    if len(ids) < 2:
      return False
    if L[ids[0]] > 0:
      for val in [L[i] for i in ids]:
        if val < 0:
          return False
    elif L[ids[0]] < 0:
      for val in [L[i] for i in ids]:
        if val > 0:
          return False
    return True

obj = Solution()
nums = [3,1,2]
print(obj.circularArrayLoop(nums))