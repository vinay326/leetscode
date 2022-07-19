# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        
        q =[]
        q.append(root)
        while len(q)>0:
            lev = len(q)
            curr = []
            for i in range(lev):
                curr_node = q.pop(0)
                curr.append(curr_node.val)
                
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            result.append(curr)
        return result
            
        