class Solution:

  def sumGame(self,num):

    l_val, r_val = 0,0
    l_change, r_change = 0,0
    
    for val in num[:len(num)//2]:
      if val == "?":
        l_change += 1
      else:
        l_val += int(val)

    for val in num[len(num)//2:]:
      if val == "?":
        r_change += 1
      else:
        r_val += int(val)

    data = [[r_val,r_change],[l_val,l_change]]
    data.sort(key=lambda x: x[0])
    diff = data[0][0] - data[1][0]
    one_side = data[0][1] - data[1][1]

    if one_side % 2 == 0:
      if diff % 9 == 0 and diff <= (one_side*9):
        return False

    return True


obj = Solution()
num = "00??"
print(obj.sumGame(num))

