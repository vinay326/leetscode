# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        twin1, twin2 = head, prev
        res = 0
        while twin2:
            res = max(res, twin1.val + twin2.val)
            twin1, twin2 = twin1.next, twin2.next
        
        return res
            
            
        