#Given an array logs with contain space
#delimited string of words where the first
#word is the id
#reorder logs such that all letter logs
#come before digit logs, letter logs are
#sorted lexicographically, and digit logs
#maintain relative sorting


def reorderLogFiles(logs):
  digit_logs, i = [], 0
  while i < len(logs):
    logs[i] = logs[i].split(" ",1)
    if logs[i][1][0].isdigit():
      digit_logs.append(' '.join(logs[i]))
      logs = logs[:i] + logs[i+1:]
    else:
      i += 1

  logs = sorted(logs,key=lambda x: (x[1],x[0]))
  for i in range(len(logs)):
    logs[i] = ' '.join(logs[i])

  return logs + digit_logs






l = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(reorderLogFiles(l))