class Solution:
    def reverseWords(self, s: str) -> str:
        x =""
        count = 0
        a = len(s.split(" "))
        for i in s.split(" "):
            x += i[::-1]
            count +=1
            if count < a:
                x += " "
        return x
            
        
