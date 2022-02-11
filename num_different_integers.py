class Solution:

  def numDifferentIntegers(self,word):

    #48 to 57 is digits
    my_list = []
    current = ""
    for i in range(len(word)):
      if 47 < ord(word[i]) < 58:
        current += word[i]
      elif current != "":
        my_list.append(int(current))
        current = ""

    if current != "":
      my_list.append(int(current))


    return len(set(my_list))


obj = Solution()
word = "a1b01c001"
print(obj.numDifferentIntegers(word))