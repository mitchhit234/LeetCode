#given an array of integers nums, and
#an array queries of queries, return
# the result of the queries

def sumEvenAfterQueries(nums,queries):

  ret = []

  base = 0
  for i in nums:
    if i % 2 == 0:
      base += i

  for i in queries:
    if nums[i[1]] % 2 == 0:
      base -= nums[i[1]]
    
    nums[i[1]] += i[0]
    if nums[i[1]] % 2 == 0:
      base += nums[i[1]]

    ret.append(base)

  return ret


n = [1,2,3,4]
q = [[1,0],[-3,1],[-4,0],[2,3]]

print(sumEvenAfterQueries(n,q))