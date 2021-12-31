# Approach 2: Iterative
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        postorder_traversal = []
        stack = [[root, False]]
        while stack:
            curr, visited = stack.pop()
            if visited:
                postorder_traversal.append(curr.val)
            else:
                stack.append([curr, True])
                children = len(curr.children)
                for i in range(children - 1, -1, -1):
                    stack.append([curr.children[i], False])
        return postorder_traversal