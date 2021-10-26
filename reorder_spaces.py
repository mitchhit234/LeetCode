#reorder spaces such that there are an
#even number of spaces between all words
#put any extra at the end

def reorderSpaces(text):
  spaces = text.count(' ')
  words = text.split()

  if len(words) <= 1:
    return words[0] + ' ' * len(text)-len(words[0])
  
  spaces_between = spaces // (len(words)-1)

  ret, added = "", 0
  for i in range(len(words)-1):
    ret += words[i] + spaces_between * ' '
    added += spaces_between
  
  return ret + words[-1] + (spaces-added)*' '
  
    


t = "hello   world"
print(reorderSpaces(t))