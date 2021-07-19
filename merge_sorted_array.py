#given two integer arrays that are sorted,
#return the merged sorted array

def merge(nums1,m,nums2,n):

  x = m+n-1
  while m > 0 and n > 0:
    if nums1[m-1] >= nums2[n-1]:
      nums1[x] = nums1[m-1]
      m -= 1
    else:
      nums1[x] = nums2[n-1]
      n -= 1
    x -= 1

  if n > 0:
    nums1[:n] = nums2[:n]

  return nums1





nums1 = [2,2,3,0,0,0]
m = 3
nums2 = [1,5,6]
n = 3

print(merge(nums1,m,nums2,n))
