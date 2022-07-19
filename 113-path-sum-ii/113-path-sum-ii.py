# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        result = []
        level = deque([root.val])
        sta = [(root, targetSum- root.val,[])]
        
        while len(sta) > 0:
            curr_node, s, path = sta.pop()
            path = path + [curr_node.val]
            
            if curr_node.left is None and curr_node.right is None and s == 0:
                result.append(path)
            if curr_node.right:
                sta.append((curr_node.right, s-curr_node.right.val, path))
            if curr_node.left:
                sta.append((curr_node.left, s-curr_node.left.val, path))
        return result
                
                