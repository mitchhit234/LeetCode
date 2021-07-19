#Given a string sequence and a string word,
#return the maximum k repeating value of word
#in sequence

def maxRepeating(sequence,word):

  if sequence == word:
    return 1

  mx = 0
  
  for i in range(len(sequence)-len(word)+1):

    c, j = 0, i
    while sequence[j:j+len(word)] == word and j <= len(sequence)-len(word):
      j += len(word)
      c += 1

    mx = max(mx,c)

  return mx
      



s = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"

print(maxRepeating(s,word))
