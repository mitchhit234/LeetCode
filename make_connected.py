#Return the min umber of operations needed to connect
#all the computers
class Solution:

    def makeConnected(self, n, connections):
      #Establish existing disjoint sets
      #sets = [[x] for x in range(n)]
      sets = []
      exists = [0]*n
      redundant = 0
      for edge in connections:
        #Find the current position of each
        #computer in the current sets
        exists[edge[0]] = exists[edge[1]] = 1
        e1, e2 = -1, -1
        for i in range(len(sets)):
          if edge[0] in sets[i]:
            e1 = i
          if edge[1] in sets[i]:
            e2 = i
          
          if e1 >= 0 and e2 >= 0:
            break
        #Neither could be in a set 
        if e1 < 0 and e2 < 0:
          sets.append(edge)
        #One could be in a set and another not
        elif e1 < 0:
          sets[e2].append(edge[0])  
        elif e2 < 0:
          sets[e1].append(edge[1])
        #Both could be in different sets
        else:
          #Both could already be in a set together
          if e1 != e2:
            t1, t2 = sets[e1], sets[e2]
            del sets[max(e1,e2)]
            del sets[min(e1,e2)]
            temp = t1 + t2
            sets.append(list(set(temp)))
          else:
            redundant += 1
      
      return

      #Add all the edges that weren't visited as independent sets
      for i in range(len(exists)):
        if exists[i] == 0:
          sets.append([i])
      #Find the minimum operations needed to
      #join all our sets

      if len(sets) - redundant <= 1:
        return len(sets)-1
      
      return -1


obj = Solution()
n = 4
connections = [[0,1],[0,2],[1,2]]
n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
connections = [[0,1],[0,2],[0,3],[1,2]]
print(obj.makeConnected(n,connections))
