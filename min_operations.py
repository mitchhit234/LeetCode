def minOperations(logs):
  ret = 0
  for i in logs:
    if i == "../":
      if ret > 0:
        ret -= 1
    elif i != "./":
      ret += 1
  return ret