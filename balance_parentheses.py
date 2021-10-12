#return the min number of operation
#to balance a parentheses string
#'())' is balanced

def minInsertions(s):
  #find indicies where a ) needs to be added
  ind, i = [], 0
  while i < len(s):
    if s[i] == '(':
      if i+1 < len(s) and s[i+1] == ')':
        ind.append(i)
        i += 1
    i += 1

  #Make insertions, keep count
  for i in ind:
    s = s[:i+1] + ')' + s[i+1:]  
  insertions = len(ind)

  #Remove the double ) just to make the logic easier
  # i = 0
  # while i < len(s):
  #   if s[i] == ')':
  #     s = s[:i+1] + s[i+2:]
  #     i += 1
  #   i += 1
  

  return s


s = "))())("
print(minInsertions(s))
    
         
