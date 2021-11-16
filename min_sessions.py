#return the min number of work sessions
#needed to complete the tasks

def minSessions(tasks,sessionTime):
  lookup = {}
  for i in tasks:
    lookup[i] = lookup.setdefault(i,0) + 1

  return lookup


#answer should be 4
s = [2,3,3,4,4,4,5,6,7,10]
time = 12
print(minSessions(s,time))