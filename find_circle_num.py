#return the total number of provinces
#or connected cities (1 interconnected
#group of cities equals a province)

def findCircleNum(isConnected):
  cities = len(isConnected)
  seen = set()
  for i in range(cities):
    if isConnected[i] not in seen:
      

    






isConnected = [[1,1,0,1],[1,1,0,1],[0,0,1,0],[1,1,0,1]]
#isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(isConnected))