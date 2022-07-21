# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = 9999999999999999
        if root is None:
            return 0
        q = [(root, 0)]
        while len(q) > 0:
            curr_node, count = q.pop()
            
            count +=1
            if curr_node.left is None and curr_node.right is None:
                min_depth = min(min_depth, count)
            
            if curr_node.right:
                q.append((curr_node.right, count))
            if curr_node.left:
                q.append((curr_node.left, count))
                
            
        
        return min_depth