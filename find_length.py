class Solution:
    def findLength(self,nums1,nums2) -> int:
      mx = 0
      dp = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
      for i in range(len(nums1)):
        for j in range(len(nums2)):
          if nums1[i] == nums2[j]:
            dp[i][j] = 1
            if i > 0 and j > 0:
              dp[i][j] += dp[i-1][j-1]
            mx = max(mx,dp[i][j])
            
      return mx






obj = Solution()
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
print(obj.findLength(nums1,nums2))
        