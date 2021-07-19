#Determine if an input string of 
#'(', ')', '{', '}', '[' and ']'
#is valid
#open brackets must be closed by 
#the same type, and they must be
#closed in the correct order

comp = {
  '(': ')',
  '{': '}',
  '[': ']',
}

def isValid(s):
  if len(s) == 0:
    return True
  
  stack = []
  for i in s:
    if i in comp.keys():
      stack.append(i)
    elif i in comp.values():
      if len(stack) == 0 or comp[stack.pop()] != i:
        return False
    else:
      return False
  return len(stack) == 0


s = "()[]{}"
print(isValid(s))
