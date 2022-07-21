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
            
            
            univalue =True
            if node.left:
                left=helper(node.left)
                univalue = left and univalue and node.left and node.val == node.left.val
            if node.right:
                right=helper(node.right)
                univalue = right and univalue and node.right and node.val == node.right.val
                
            if univalue:
                count +=1
            return univalue
            
        count = 0
        helper(root)
        return count