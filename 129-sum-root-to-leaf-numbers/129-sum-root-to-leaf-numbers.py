# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
            def dfs(curr_node, r, result_sum):
                if curr_node is None:
                    return result_sum
                    
                r = r * 10 + curr_node.val
                
                if curr_node.right is None and curr_node.left is None:
                         result_sum += r
                         return result_sum

                return dfs(curr_node.left,r, result_sum) + dfs(curr_node.right, r, result_sum)
            x=dfs(root, 0, 0)
            return x
        