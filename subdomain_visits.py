class Solution:
  def subdomainVisits(self,cpdomains):

    L = {}
    for i in cpdomains:
      parsed = i.split(" ")
      count = int(parsed[0])
      domain = parsed[1]

      while domain:
        if domain in L:
          L[domain] += count
        else:
          L[domain] = count11111111
        
        nxt = domain.find('.')
        if nxt > -1:
          domain = domain[nxt+1:]
        else:
          domain = ""

    ret = []
    for key in L:
      ret.append(str(L[key]) + " " + key)


    return ret




obj = Solution()
cpdomains = ["9001 discuss.leetcode.com"]
print(obj.subdomainVisits(cpdomains))