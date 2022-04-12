# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        q = collections.deque([(root, TreeNode(1), TreeNode(1))])
        
        while q:
            curr, parent, grandparent = q.popleft()
            if curr:
                if grandparent.val % 2 == 0:
                    res += curr.val
                if curr.left:
                    q.append((curr.left, curr, parent))
                if curr.right:
                    q.append((curr.right, curr, parent))
        return res