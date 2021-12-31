"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def recursive(node):
            if node is None:
                return []
            for child in node.children:
                recursive(child)
            result.append(node.val)
        
        
        
        
        
        
        result = []
        recursive(root)
        
        return result
         
          
        
        
        
        
        
       
        