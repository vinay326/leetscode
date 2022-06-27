# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = ListNode(0,head)
        curr = temp
        while curr.next != slow:
            curr = curr.next
        curr.next = slow.next
        curr  = curr.next

        return  temp.next
        