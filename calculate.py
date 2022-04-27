class Solution:

  def calculate(self, s):
      if not s:
          return "0"
      stack, num, sign = [], 0, "+"
      for i in range(len(s)):
          if s[i].isdigit():
              num = num*10+ord(s[i])-ord("0")
          if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
              if sign == "-":
                  stack.append(-num)
              elif sign == "+":
                  stack.append(num)
              elif sign == "*":
                  stack.append(stack.pop()*num)
              else:
                  tmp = stack.pop()
                  if tmp//num < 0 and tmp%num != 0:
                      stack.append(tmp//num+1)
                  else:
                      stack.append(tmp//num)
              sign = s[i]
              num = 0
      return sum(stack)

# class Solution:

#   def calculate(self, s):
#     s = self.parse(s)

#     index = 0
#     while index < len(s):
#       if s[index] == "*" or s[index] == "/":
#         s = self.operation(s,index) 
#         index -= 2
#       index += 1

#     index = 0
#     while index < len(s):
#       if s[index] == "+" or s[index] == "-":
#         s = self.operation(s,index) 
#         index -= 2
#       index += 1

#     return int(s[0])


#   def parse(self,s):
#     ret = []
#     flags = ["+","-","*","/"," "]
#     current = ""
#     for i in range(len(s)):
#       if s[i] not in flags:
#         current += s[i]
#       else:
#         if len(current) > 0:
#           ret += [current]
#         if s[i] != flags[-1]:
#           ret += s[i]
#         current = ""
    
#     if len(current) > 0:
#       ret += [current]

#     return ret




#   def operation(self,s,i):
#     t1, t2 = int(s[i-1]), int(s[i+1])
#     result = 0
#     if s[i] == "*":
#       result = t1*t2
#     elif s[i] == "/":
#       result = t1//t2
#     elif s[i] == "+":
#       result = t1+t2   
#     else:
#       result = t1-t2

#     s = s[:i-1] + [result] + s[i+2:]


#     return s




obj = Solution()
s = "3+5 / 2"
print(obj.calculate(s))