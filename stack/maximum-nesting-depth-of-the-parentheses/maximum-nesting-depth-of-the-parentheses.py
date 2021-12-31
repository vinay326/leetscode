class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []
        
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(s[i])
                if len(stack) > max_depth:
                    max_depth = len(stack)
            elif s[i] == ')':
                stack.pop()
            
        return max_depth
        