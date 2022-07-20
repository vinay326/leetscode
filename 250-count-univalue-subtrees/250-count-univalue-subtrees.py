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
            if root.left == None and root.right == None:
                count +=1
                return True
            isUnivalue =  True
            
            if node.left:
                left = helper(node.left)
                isUnivalue = left and isUnivalue and node.val == node.left.val
            
            if node.right:
                right = helper(node.right)
                isUnivalue = right and isUnivalue and node.val == node.right.val
            
            if isUnivalue:
                count +=1
                return isUnivalue
        count = 0   
        helper(root)
        return count
        