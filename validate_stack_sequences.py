#Given two sequences with distinct values,
#return true if and only if this could have been
#the result of push and pop operations on an
#initially empty stack

def validateStackSequences(pushed, popped):
  stack = []
  i, j = 0, 0
  while i < len(pushed):
    if len(stack) > 0 and stack[0] == popped[j]:
        stack = stack[1:]
        i -= 1
        j += 1
    elif pushed[i] != popped[j]:
      stack = [pushed[i]] + stack
    else:
      j += 1
    i += 1
  
  return True if stack == popped[j:] else False

  
    


pu = [1,2,3,4,5]
po = [4,3,5,1,2]
print(validateStackSequences(pu,po))
