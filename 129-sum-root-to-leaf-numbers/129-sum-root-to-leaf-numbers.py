# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = [(root, 0)]
        result_sum = 0
        while len(s) > 0:
            curr_node, r = s.pop()
            r = r * 10 + curr_node.val
            
            if curr_node.right is None and curr_node.left is None:
                     result_sum += r
            
            if curr_node.right:
                s.append((curr_node.right, r))
            if curr_node.left:
                s.append((curr_node.left, r))
        
        return result_sum