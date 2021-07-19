#Given a non empty list of integers digits,
#return the list as the entire number incremented by 
#one digit

def plusOne(digits):
  i = len(digits) - 1
  if i < 0:
    return [1]
  
  if digits[i] < 9:
    digits[i] += 1
  else:
    return plusOne(digits[:-1]) + [0]

  return digits
    










digits = [0]
print(plusOne(digits))