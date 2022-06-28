class Solution:
    def isPalindrome(self, s: str) -> bool:
        x =''.join(e.lower() for e in s if e.isalnum())
        
        return x == x[::-1]
        
        