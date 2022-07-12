# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = []
        result = -999999
        count =0
        q.append(root)
        
        if root is None:
            return 0
        
        while len(q) > 0:
            count +=1
            level = len(q)
            for i in range(level):
                curr_node = q.pop(0)
                
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                    
                if (curr_node.left is None) and (curr_node.right is None):
                    result = max(result, count)
        return result         