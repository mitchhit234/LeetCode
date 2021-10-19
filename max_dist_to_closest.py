#Given an array of people in seats,
#determine the seat that has the maximum
#distance from anyone else in a seat,
#and return that distance

import math

def maxDistToClosest(seats):
  #Catch the cases where the longest distance
  #is not contained by a set of 1's
  beg, end = 1, 1
  
  if seats[0] == 0:
    i = 1
    while seats[i] == 0:
      beg += 1
      i += 1

  if seats[-1] == 0:
    i = len(seats)-2
    while seats[i] == 0:
      end += 1
      i -= 1

  mx = max(beg,end)

  #Find the longest string of 0's
  longest, count = 0, 0
  for i in seats:
    if i == 0:
      count += 1
    else:
      longest = max(longest,count)
      count = 0
  
  #return half the longest strech of
  #empty chairs or a strech of empty 
  #chairs at the end if its larger
  return max(mx,math.ceil(longest/2))

  

s = [0,0,0,0,1,0,1,0,0]
print(maxDistToClosest(s))
  
