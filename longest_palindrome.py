#Given a string s return the 
#longest palindromic substring in s

def longestPalindrome(s):
  if len(s) <= 1:
    return s
  if len(s) == 2:
    if s[0] == s[1]:
      return s
    return s[0]

  #Odd length palindrome will have one
  #middle unique letter
  #Even length palindrome will have
  #two same letters back to back
  evens, odds = [], []
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      evens.append(i)
  
  for i in range(len(s)-2):
    if s[i] == s[i+2]:
      odds.append(i)


  mx, mx_str = 0, ""
  for i in evens:
    count = 0
    left, right = i, i+1
    while (left >= 0 and right < len(s)) and s[left] == s[right]:
      count += 1
      left -= 1
      right += 1

    if count > mx:
      mx_str = s[left+1:right]
      mx = count  

  for i in odds:
    count = 0
    left, right = i, i+2
    while (left >= 0 and right < len(s)) and s[left] == s[right]:
      count += 1
      left -= 1
      right += 1

    if count >= mx:
      mx_str = s[left+1:right]
      mx = count  

  return mx_str if len(mx_str) > 0 else s[0]
  

s = "ccc"
print(longestPalindrome(s))

  
