class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



#Delete from index a to b in list1, insert
#list 2 in its place
def mergeInBetween(list1,a,b,list2):
  a = traverse(list1,a,b,list2)
  return a
  

def traverse(list1,a,b,list2):
  if a > 0:
    return ListNode(list1.val,traverse(list1.next,a-1,b-1,list2))
  if list2:
    return ListNode(list2.val,traverse(list1,a,b,list2.next))
  
  temp_list = list1.next
  if b > 0:
    while b > 0:
      temp_list = temp_list.next
      b -= 1
  
  return temp_list
  





list1 = ListNode(0,ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))
list2 = ListNode(1000000,ListNode(1000001,ListNode(1000002)))
a = 3
b = 4
print(mergeInBetween(list1,a,b,list2))