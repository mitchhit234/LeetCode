#given two sorted arrays of size m and n
#find the median of the two sorted arrays
#in O(log(m+n)) time

def findMedianSortedArrays(nums1,nums2):
  if len(nums1) > len(nums2):
    temp = nums1
    nums1 = nums2
    nums2 = temp
  
  j = len(nums2)//2
  lo, hi = 0, len(nums1)-1
  while lo <= hi:
    mid = lo + (hi-lo)//2
    diff = (len(nums1)-(mid+1)) - (mid+1)
    x_low, x_high = nums1[mid], nums1[mid+1]
    y_low, y_high = nums2[j+diff], nums2[j+diff+1]
    if x_low <= y_high and y_low <= x_high:
      if len(nums1) + len(nums2) % 2 == 0:
        return (x_low + y_high)/2
      return max(x_low,y_high)
    elif y_low > x_high:
      lo = mid+1
    else:
      hi = mid


  







a = [1,3]
b = [2]

# a = [3,7,9,15,18,21,25]
# b = [4,6,8,10,11,18]
print(findMedianSortedArrays(a,b))