# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
          def count_sum_nodes(root):
                if root.val >= low and root.val <= high:
                    self.ans += root.val
                if root.left:
                    count_sum_nodes(root.left)
                if root.right:
                    count_sum_nodes(root.right)
          self.ans = 0     
          count_sum_nodes(root)
          return self.ans
        
                