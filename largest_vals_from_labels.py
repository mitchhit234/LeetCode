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
      if lookup_table[j] != 0:
        count += values[i]
        lookup_table[j] -= 1
        lookup[values[i]].remove(j)
        num_wanted -= 1
    i += 1

  return count


values = [3,0,3,0,6]
labels = [0,2,1,1,0]
num_wanted = 4
use_limit = 1
print(largestValsFromLabels(values,labels,num_wanted,use_limit))