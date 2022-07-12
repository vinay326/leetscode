# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if root is None:
            return result
        q = []
        q.append(root)
        while len(q) > 0:
            level = len(q)
            curr_level = 0
            for i in range(level):
                curr_node = q.pop(0)
                curr_level += curr_node.val
                
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            if curr_node == root:
                result.append(curr_level)
            else:
                result.append(curr_level/level)
        return result
        