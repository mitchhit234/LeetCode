#merge two sorted linked lists as
#one sorted linked list


#Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
      a = ListNode()
      if l1 and l2:
        if l1.val < l2.val:
          a.val = l1.val
          a.next = self.mergeTwoLists(l1.next,l2)
        else:
          a.val = l2.val
          a.next = self.mergeTwoLists(l1,l2.next)

      elif not l1:
        a = l2
      else:
        a = l1
      
      return a


  
      


      

l1 = ListNode(1,ListNode(2,ListNode(4,None)))
l2 = ListNode(1,ListNode(3,ListNode(4,None)))


a = Solution().mergeTwoLists(l1,l2)
g = 0
