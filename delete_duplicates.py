#given the head of a sorted linked list,
#remove all duplicates so that each element
#only appears once. return the resulting sorted list

from remove_duplicates import removeDuplicates


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
  if head == None:
    return head
  if head.next == None:
    return head

  if head.val == head.next.val:
    head = deleteDuplicates(head.next)
  else:
    head.next = deleteDuplicates(head.next)

  
  return head



