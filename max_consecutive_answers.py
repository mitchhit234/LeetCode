import collections
#Try to find the max number of consecutive True s
#or False s with k operations on the string
def maxConsecutiveAnswers(s,k):
  maxf = i = 0
  count = collections.Counter()
  for j in range(len(s)):
      count[s[j]] += 1
      maxf = max(maxf, count[s[j]])
      if j - i + 1 > maxf + k:
          count[s[i]] -= 1
          i += 1
  return len(s) - i






  return 0




answerKey = "TTFFTT"
k = 2
print(maxConsecutiveAnswers(answerKey,k))
