#remove integers from an array if they are 
#duplicates of previous values
#array input is in ascending order

# def removeDuplicates(nums):
#   i = 0
#   for index in range(1,len(nums)):
#     if nums[index] != nums[i]:
#       i+=1
#       nums[i] = nums[index]
#   return i+1


# print(removeDuplicates([1,1,2]))


#Given a string s and integer k,
def removeDuplicates(s,k):
  done = False
  while not done:
    done, i, count = True, 1, 1
    while i < len(s):
      if s[i] == s[i-1]:
        count += 1
        if count >= k:
          s = s[:i-k+1] + s[i+1:]
          i = max(i-k,0)
          done = False
          count = 1
      else:
        count = 1
      i += 1
  return s


s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(s,k))