# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
   
        def helper(node):
            nonlocal count
            if node.left is None and node.right is None:
                count +=1
                return True
            
 
            isunivalue = True
            if node.left:
                left = helper(node.left)
                isunivalue = left and isunivalue and node.left and node.val == node.left.val
            
            if node.right:
                right = helper(node.right)
                isunivalue = right and isunivalue and node.right and node.val == node.right.val
            
            if isunivalue:
                count +=1
            return isunivalue
        
        count = 0
        helper(root)
        return count
            
            