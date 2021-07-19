#Given a string sentence containing only
#lower case english letters,
#return true if sentence is a pangram

def checkIfPangram(sentence):
  store = [0] * 26
  for i in sentence:
    store[ord(i)-97] = 1
  return False if 0 in store else True
    

s = "leetcode"
print(checkIfPangram(s))