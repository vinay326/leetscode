# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        result = []
        if root is None:
            return result
        q = []
        q.append(root)
        q.append(None)
        levels = deque()
        traversal = True
        while len(q) > 0:
            curr_node = q.pop(0)
            if curr_node:
                if traversal:
                    levels.append(curr_node.val)
                else:
                    levels.appendleft(curr_node.val)
                
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            else:
                result.append(levels)
                if len(q) > 0:
                    q.append(None)
                levels = deque()
                traversal = not traversal
        return result