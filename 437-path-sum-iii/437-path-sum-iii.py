# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
            result = 0
            def dfs(node: Optional[TreeNode]) -> List[int]:
                nonlocal result

                if not node: return []

                l = dfs(node.left)
                r = dfs(node.right)

                sums = [ n+node.val for n in (l+r) ] + [node.val]
                result += sums.count(targetSum)

                return sums

            dfs(root)

            return result
