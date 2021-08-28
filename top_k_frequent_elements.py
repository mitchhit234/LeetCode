#Given an integer array nums and an integer , return the k most frequent elements


def topKFrequent(nums,k):
  lookup = dict()

  start = len(nums)
  mt = [0]*(start+1)

  for i in nums:
    lookup[i] = lookup.get(i,0) + 1

  mx_elements, i = [], 0
  for key in lookup:
    count = lookup[key]
    if mt[count] == 0:
      mt[count] = [key]
    else:
      mt[count].append(key)

  ret = []
  for i in range(start,-1,-1):
    if k < len(ret):
      break
    if mt[i] != 0:
      for j in mt[i]:
        ret.append(j)

  return ret[:k]





n = [1]
k = 1
print(topKFrequent(n,k))