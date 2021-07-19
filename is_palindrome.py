#Given the head od a linked list,
#return true if palindrome


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
  rev = None
  fast = slow = head
  while fast != None and fast.next != None:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next

  if fast != None:
    slow = slow.next

  while slow != None or rev != None:
    if slow.val == rev.val:
      slow = slow.next
      rev = rev.next
    else:
      return False
  
  return slow == None and rev == None
  

  

l = ListNode(1,ListNode(1))
print(isPalindrome(l))