class Solution:

  def longestSubstring(self,s: str, k: int) -> int:
    if len(s) < k:
      return 0
 
    mn = min(s,key=s.count)
    if s.count(mn) >= k:
      return len(s)
    
    mx = 0
    for i in s.split(mn):
      mx = max(mx,self.longestSubstring(i,k))
    
    return mx




sol = Solution()
s = "aaabb"
k = 3
print(sol.longestSubstring(s,k))