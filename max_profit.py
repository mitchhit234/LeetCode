#Given an array prices where 
#prices[i] is the price of stock
#on the ith day
#Return maximized profit from buying and
#selling on any day

def maxProfit(prices):
  smallest, max_profit = 10**5, 0
  for i in range(len(prices)):
    smallest = min(smallest, prices[i])
    max_profit = max(max_profit,prices[i]-smallest)
    
  return max_profit
  
prices = [7,1,5,3,6,4]
print(maxProfit(prices))