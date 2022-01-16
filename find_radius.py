#Given the position of houses and 
#heaters, return the min radius
#of all heaters that can cover all houses
def findRadius(houses,heaters):
  houses = sorted(houses)
  heaters = sorted(heaters)

  mx = 0
  for i in houses:
    for jindex, j in enumerate(heaters):
      if j > i:
        if jindex == 0:
          mx = max(j-i,mx)
        else:
          temp = min(j-i,i-heaters[jindex-1])
          mx = max(temp,mx)
          heaters = heaters[jindex-1:]

        break  
      elif jindex == len(heaters)-1:
        mx = max(i-heaters[jindex],mx)

    

  return mx





houses = [1,2,3,4]
heaters = [1,4]

print(findRadius(houses,heaters))