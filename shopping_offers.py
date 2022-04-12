class Solution:

  def shoppingOffers(self, price, special, needs):
    
    total_comp = 0
    for i in range(len(price)):
      total_comp += (price[i]*needs[i])
    

    return self.rec(price, special, needs, total_comp)


  def rec(self,price,specials,needs,total):

    for special in specials:
      valid = True
      total_now = 0
      transform = []
      for index, amount in enumerate(special[:-1]):
        total_now += (price[index]*amount)
        transform.append(amount)
        if amount > needs[index]:
          valid = False
          break
      if valid:
        if total_now < special[-1]:
          for index in range(len(transform)):
            needs[index] -= transform[index]
            




obj = Solution()
price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print(obj.shoppingOffers(price,special,needs))