#given a set of values and labels
#return the largest possible sum of
#the subset S

def largestValsFromLabels(values,labels,num_wanted,use_limit):
  lookup = {}
  lookup_table = [use_limit] * (max(labels)+1)
  for i in range(len(labels)):
    lookup[values[i]] = lookup.get(values[i],[]) + [labels[i]]
    
  values = sorted(values,reverse=True)

  count, i = 0, 0
  while num_wanted > 0 and i < len(values):
    for j in lookup[values[i]]:
      if lookup_table[j] != 0 and num_wanted > 0:
        count += values[i]
        lookup_table[j] -= 1
        lookup[values[i]].remove(j)
        num_wanted -= 1
    i += 1

  return count


values = [7,5,6,6,4,4,0,0,6]
labels = [1,1,0,2,0,0,0,0,2]
num_wanted = 2
use_limit = 3
print(largestValsFromLabels(values,labels,num_wanted,use_limit))