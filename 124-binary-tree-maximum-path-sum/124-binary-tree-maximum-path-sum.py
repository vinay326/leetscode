# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -9999999999
        
        def helper( node):
            if not node:
                return 0

            else:

                left_sum = helper( node.left )
                right_sum = helper( node.right )
                
                left_sum = max(left_sum, 0)
                right_sum = max(right_sum, 0)
                
                
                x = node.val + left_sum + right_sum 
                
                
                
                nonlocal max_sum
                max_sum = max(max_sum, x)
                
                return node.val + max(left_sum, right_sum)
        
        helper( root )
        
        return max_sum
        