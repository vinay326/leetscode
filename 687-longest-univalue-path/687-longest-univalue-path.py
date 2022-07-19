# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest_uni_path = 0
        
        def helper( node):
            if not node:
                return 0

            else:

                path_of_left = helper( node.left )
                path_of_right = helper( node.right )
                
                left_uni = path_of_left+1 if node.left and node.left.val == node.val else 0
                
                right_uni = path_of_right+1 if node.right and node.right.val == node.val else 0
        
                nonlocal longest_uni_path
            
                longest_uni_path = max( longest_uni_path, left_uni + right_uni )

                return max(left_uni, right_uni)   
        
        helper( root )
        
        return longest_uni_path
        
        