# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pred = temp = ListNode(0, head)
        prev,curr = None,head
        count = 0
        while curr:
            count +=1
            if count == left:
                x = curr
                while curr:
                    a = curr.next
                    curr.next = prev
                    prev = curr
                    if count == right:
                        curr = a
                        break
                    curr = a
                    count +=1
                x.next = curr
                pred.next = prev
            else:
                pred = pred.next
                curr = curr.next
            
                
        return temp.next
                
        