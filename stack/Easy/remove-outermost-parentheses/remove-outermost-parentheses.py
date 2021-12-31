class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        a=""
        b=0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                stack.pop()
            
            if len(stack) == 0:
                a = a + s[b+1:i]
                b=i+1
        return a 
                
        