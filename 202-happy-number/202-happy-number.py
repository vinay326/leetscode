class Solution:
    def isHappy(self, n: int) -> bool:
        def get_total(n):
            sum = 0
            while n > 0:
                n, rem = divmod(n, 10)
                sum += rem *rem
            return sum
        slow = n
        fast = get_total(n)
        while fast!=1 and fast !=slow:
            slow = get_total(slow)
            fast = get_total(get_total(fast))
        return fast == 1
                
                    
            
        
        