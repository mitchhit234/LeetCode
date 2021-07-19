#an array in a mountian if
#array length >= 3
#there exists some i 0 < 1 < array length - 1
#such that an i less is less in array value
#as well as an i greater is less in array value



def peakIndexInMountainArray(arr):
  lower, upper = 0, len(arr)-1
  while lower != upper:
    mid = lower + ((upper - lower) // 2)
    if arr[mid] < arr[mid+1]:
      lower = mid+1
    else:
      upper = mid 
  
  return lower

  

a = [0,2,1,0]
print(peakIndexInMountainArray(a))