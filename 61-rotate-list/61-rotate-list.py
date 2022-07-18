# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
            if head is None:
                return head
            
            temp = head
            n = 1
            while temp.next:
                temp = temp.next
                n +=1
            temp.next = head
            
            new_tail = head
            for i in range(n-k % n-1):
                new_tail = new_tail.next
            
            head = new_tail.next
            
            new_tail.next = None
            
            return head
            
    
            
                
                
                
            
        
        
        