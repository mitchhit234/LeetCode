class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head):
  slow, fast = head, head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  #Slow is now the halfway point
  #Reverse the second half of the linked list
  prev, curr, nxt = None, slow, None
  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

  #Iterate through and find the max pairSum
  mx = 0
  while head and prev:
    mx = max(head.val+prev.val,mx)
    head, prev = head.next,prev.next

  return mx
  
  
r = ListNode(47,ListNode(81,ListNode(81,ListNode(9))))

#r = ListNode(5,ListNode(4,ListNode(2,ListNode(1))))
print(pairSum(r))


  
  