#Consider a graph of nodes 0-n with
#red edfes abd blue edges as input
#return an array answer of length n
#where each index is the length of the
#shortest path from 0 to i such that
#edge colors are alternating along the path
#or -1 if no path exists

def shortestAlternatingPaths(n,red_edges,blue_edges):
  ret = [[500,0]] * n
  ret[0] = [0,0]
  stack = [0]
  while len(stack) != 0:
    node = stack[0]
    length = ret[node]
    if length[1] != 1:
      for i in red_edges:
        if i[0] == node:
          stack.append(i[1])
          ret[i[1]] = [length[0]+1,1]
          red_edges.remove(i)
        elif i[1] == node:
          stack.append(i[0])
          ret[i[1]] = [length[0]+1,1]
          red_edges.remove(i)
    if length[1] != -1:
      for i in blue_edges:
        if i[0] == node:
          stack.append(i[1])
        elif i[1] == node:
          stack.append(i[0])
    stack = stack[1:]












n = 3
red_edges = [[0,1]]
blue_edges = [[2,1]]
print(shortestAlternatingPaths(n,red_edges,blue_edges))
