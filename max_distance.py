def maxDistance(nums1,nums2):
  ret = 0
  for i in range(len(nums1)):
    j = i + ret
    while j < len(nums2) and nums1[i] <= nums2[j]:
      j += 1
    ret = max(ret,j-i-1)
    
  return ret


nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
nums1 = [2,2,2]
nums2 = [10,10,1]
# nums1 = [30,29,19,5]
# nums2 = [25,25,25,25,25]
print(maxDistance(nums1,nums2))