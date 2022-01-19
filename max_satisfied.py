#return the max number of customers that can be
#satisfied
def maxSatisfied(customers,grumpy,minutes):
  #Determine already satisfied, alter grumpy
  #to find out how much your missing at each index
  n = len(customers)
  satisfied = 0
  for i in range(min(minutes,n)):
    if grumpy[i] == 0:
      satisfied += customers[i]
    else:
      grumpy[i] = customers[i]

  if minutes < n:
    current = sum([grumpy[x] for x in range(minutes)])
    mx = current
    to_add = 0
    for i in range(minutes,n):
      to_add += 1
      if grumpy[i] == 0:
        satisfied += customers[i]
      else:
        grumpy[i] = customers[i]
      current -= grumpy[i-minutes]
      current += grumpy[i]
      mx = max(mx,current)
    
    satisfied += mx

  else:
    satisfied += sum(grumpy)


  
  return satisfied


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
customers = [1]
grumpy = [0]
minutes = 1
print(maxSatisfied(customers,grumpy,minutes))