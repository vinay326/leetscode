# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        count = 0
        result = []
        max = -999
        while head:
            count +=1
            result.append(head.val)
            head = head.next
            
        for i in range(count//2):
            a = result[i] + result[count-i-1]
            if a > max:
                max = a
        return max
            
            