# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        result = {}
        temp = ListNode(0, head)
        pred = temp
        curr = head
        while curr:
            if curr.val not in result:
                result[curr.val] =0
            result[curr.val] +=1
            curr = curr.next
        
        while head:
            if head.val in result and result[head.val] > 1:
                    pred.next =  head.next
            else:
                pred=pred.next
                    
            
            head = head.next
        return temp.next
            
                
                
        
                