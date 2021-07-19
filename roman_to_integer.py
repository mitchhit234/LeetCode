#Given a roman numeral,
#turn it into an integer

lookup = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000
}

def romanToInt(s):
  ret = 0
  for index, value in enumerate(s):
    if lookup[value] > lookup[s[index-1]] and index > 0:
      if lookup[s[index-1]] * 5 == lookup[value]:
        ret += 3*lookup[s[index-1]]
      else:
        ret += 8*lookup[s[index-1]]
    else:
      ret += lookup[value]
  return ret 





print(romanToInt("MCMXCIV"))