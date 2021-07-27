#Given two gene strings start and end and the gene bank,
#return the minimum number of mutations needed to mutate
#from start to end. If none, return -1
#starting point is assumed valid

def minMutation(start, end, bank):
  if start == end:
    return 0
  current, visited = [start], []
  step = 0
  while end not in current and len(current) > 0:
    to = len(current)
    for i in range(to):
      l = current.pop(0)
      visited.append(l)
      for j in bank:
        diff = 0
        for c1, c2 in zip(l,j):
          if c1 != c2:
            diff += 1
        if diff == 1:
          if j not in visited:
            current.append(j)
    step += 1
  if end not in current:
    return -1
  return step if step > 0 else -1
        

s = "AAAAAAAA"
e = "CCCCCCCC"
b = ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA"]
print(minMutation(s,e,b))