#Return the number to its word representation
#Numbers all the way up to the billions

class Solution:
    def numberToWords(self, num: int) -> str:

      normal = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
      teens = ["","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
      prefixes = ["","","Twen","Thir","Four","Fif","Six","Seven","Eigh","Nine"]
      suffix = "ty"
      classify = ["Hundred","Thousand","Million","Billion"]


      #Every three digits starting from smallest
      #to largest will be normal form, teens/prefixes+suffix,
      #then normal form with classification 
      ret = []
      position = 1
      while num > 0:
        digit = num % 10
        if position % 3 == 1:
          ret += [normal[digit]]

        elif position % 3 == 2:
          if digit == 1:
            ret[len(ret)-1] = teens[digit]
          else:
            ret += [prefixes[digit]+suffix]

        else:
          if digit > 0:
            cl = position // 3
            ret += [classify[cl]] + [normal[digit]]

        num //= 10
        position += 1

      return " ".join(ret[::-1])




obj = Solution()
num = 1234567
print(obj.numberToWords(num))
