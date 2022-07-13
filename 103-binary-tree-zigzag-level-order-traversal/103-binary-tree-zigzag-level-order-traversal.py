# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        q = []
        q.append(root)
        depth = 0
        direction = "right"
        while len(q) > 0:
            depth += 1
            level = len(q)
            curr_level = []
            for i in range(level):
                curr_node = q.pop(0)
                curr_level.append(curr_node.val)
     
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)               
            if depth % 2 == 0:
                curr_level = curr_level[::-1]
            result.append(curr_level)
        return result
    