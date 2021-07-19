#given a string s of zeros and ones
#return the maximum score after splitting
#the string into two non empty strings

def maxScore(s):
  zeros, ones, score = 0, 0, 0
  for i in range(len(s)):
    if s[i] == "0":
      zeros += 1
    else:
      ones += 1
    if i < len(s)-1:
      score = max(zeros-ones,score)
  
  return ones + score
    

s = "000101"
print(maxScore(s))