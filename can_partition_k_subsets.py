#given an integer array numns and an integer k
#return true if its possible to divide array into
#k non empty subsets who sums are all equal

class Solution:

  def canPartitionKSubsets(self,nums,k):
    sums = [0]*k
    subsum = sum(nums) / k
    nums.sort(reverse=True)
    l = len(nums)
    
    def walk(i):
        if i == l:
            return len(set(sums)) == 1
        for j in range(k):
            sums[j] += nums[i]
            if sums[j] <= subsum and walk(i+1):
                return True
            sums[j] -= nums[i]
            if sums[j] == 0:
                break
        return False        
    
    return walk(0)



obj = Solution()
nums = [4,3,2,3,5,2,1]
k = 4
print(obj.canPartitionKSubsets(nums,k))




  