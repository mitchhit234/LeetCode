#Find the total number of combinations of coins that
#totals to x amount of money

def change(amount,coins):
  dp = [0]* (amount+1)
  dp[0] = 1
  for i in coins:
    for j in range(i, amount + 1):
      dp[j] += dp[j - i]
  return dp[amount]




amount = 5
coins = [1,2,5]
print(change(amount,coins))

