#a bug's home is on the x axis at position x
#it starts at 0, can jump a positions forward and
#b positions backward
#it can not jump to any integer in the array forbidden
#and it can not jump backward twice in a row
#return the minimum number of jumps needed for
#the bug to reach home, if not possible return -1

from collections import deque 

def minimumJumps(forbidden,a,b,x):
    dq, seen, steps, furthest = deque([(True, 0)]), {(True, 0)}, 0, max(x, max(forbidden)) + a + b
    for pos in forbidden:
        seen.add((True, pos)) 
        seen.add((False, pos)) 
    while dq:
        for _ in range(len(dq)):
            dir, pos = dq.popleft()
            if pos == x:
                return steps
            forward, backward = (True, pos + a), (False, pos - b)
            if pos + a <= furthest and forward not in seen:
                seen.add(forward)
                dq.append(forward)
            if dir and pos - b > 0 and backward not in seen:
                seen.add(backward)
                dq.append(backward)    
        steps += 1         
    return -1

def minimumJumps2(forbidden,a,b,x):
  step = 0
  mx = a + b + max(x, max(forbidden))
  a, b = traverse(forbidden,a,b,x,0,False,mx,step)
  if a < 0:
    return -1
  return a


def traverse(forbidden,a,b,x,c,prev_back,mx,step):
  step += 1
  if c < 0:
    return step, False
  elif c in forbidden:
    return step, False
  elif c >= mx:
    return step, False
  elif c == x:
    return step, True

  if not prev_back:
    step1, left = traverse(forbidden,a,b,x,c-b,True,mx,step)
  else:
    step1, left = 0, False
  step2, right = traverse(forbidden,a,b,x,c+a,False,mx,step)

  ret = 0
  if left and right:
    ret = min(step1,step2)
  elif left and not right:
    ret = step1
  elif right and not left:
    ret = step2
  else:
    ret = -99999

  return ret, (left or right)






forbidden = [1,6,2,14,5,17,4]
a = 16
b = 9
x = 7
print(minimumJumps2(forbidden,a,b,x))