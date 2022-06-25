# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next is not None:
            slow = slow.next
            fast=fast.next.next
            if fast == slow:
                curr = head
                while curr is not slow:
                    curr = curr.next
                    slow = slow.next
                return slow
        return None
    
    