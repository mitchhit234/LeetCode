#Given two integer arrays nums1 and nums2
#return the max length of a subarray
#that appears in both arrays


def findLength(nums1,nums2):
  mem = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
  for i in range(len(nums1)-1,-1,-1):
    for j in range(len(nums2)-1,-1,-1):
      if nums1[i] == nums2[j]:
        mem[i][j] = mem[i+1][j+1] + 1
  mx = 0
  for i in mem:
    for j in i:
      mx = max(j,mx)
  return mx




n1 = [1,2,3,2,1]
n2 = [3,2,1,4,7]
print(findLength(n1,n2))