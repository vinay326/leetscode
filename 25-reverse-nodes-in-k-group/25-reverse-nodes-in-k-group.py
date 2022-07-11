# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverse_linkedlist(self,head, k):
        prev, curr = None, head
        while k:
            a = curr.next
            curr.next = prev
            prev = curr
            curr = a
            k -=1
        return prev
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev, curr = None, head
        pred=temp = ListNode(0, head)      
        if k == 1 :
            return head
        
        while curr:
            count = 0 
            new_head = curr
            while count < k and curr:
                curr = curr.next
                count +=1
            
            if count == k:
                rev_head = self.reverse_linkedlist(new_head,k)
                pred.next = rev_head
                while rev_head.next:
                    rev_head = rev_head.next
                pred = rev_head
                new_head.next = curr
        
        return temp.next        
                
            
            
                
            
                
                
            
            
                
                
        
           
                

            
        

            

        return temp.next