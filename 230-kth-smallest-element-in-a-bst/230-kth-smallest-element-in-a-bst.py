# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result =[]
        def smalles_val(root):
            if root is None:
                return None
            else:
                self.result.append(root.val)
            if root.left:
                smalles_val(root.left)
            if root.right:
                smalles_val(root.right)
        
        smalles_val(root)
        self.result.sort()
        return self.result[k-1]    
                
        