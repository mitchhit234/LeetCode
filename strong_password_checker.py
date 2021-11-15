#Given a password, return the min number
#of steps required to make the password strong
#Steps can be insertions, deletions, or replacements

#Between 6 and 20 Characters
#Contains one lowercase letter, one upper case, and one digit
#Does not contain 3 repeating characters

def strongPasswordChecker(password):
  #length requirement
  num_add = 6 - len(password) if len(password) < 6 else 0
  num_remove = len(password) - 20 if len(password) > 20 else 0

  #lowercase, uppercase, digit exist
  special = [1,1,1]
  for i in password:
    if 96 < ord(i) < 123:
      special[0] = 0
    elif 64 < ord(i) < 91:
      special[1] = 0
    elif ord(i) != 46 and ord(i) != 33:
      special[2] = 0
  rep_spec = sum(special)

  rep_need = 0
  current, count = "", 1
  #find repeations of 3 or more
  for i in password:
    if i == current:
      count += 1
      if count == 3:
        rep_need += 1
        count = 0
    else:
      count = 1
      current = i

  if num_add > 0:
    mx = max(num_add,rep_spec)
    return max(mx, rep_need-mx)
  elif num_remove > 0:
    rep_need = rep_need - num_remove
    return num_remove + max(rep_spec,rep_need)
  else:
    return max(rep_spec,rep_need)

  return 



p = "bbaaaaaaaaaaaaaaacccccc"
print(strongPasswordChecker(p))