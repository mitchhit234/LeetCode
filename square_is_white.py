def squareIsWhite(coordinates):
  #97-104 a through h
  #odds start at black, evens at white
  if ord(coordinates[0]) % 2 == int(coordinates[1]) % 2:
    return False
  return True


coordinates = "a1"
print(squareIsWhite(coordinates))