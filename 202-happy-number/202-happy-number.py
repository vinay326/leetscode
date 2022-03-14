class Solution:
    def isHappy(self, n: int) -> bool:
       def get_sum(number):
         total_sum = 0
         while number > 0:
           number, digit = divmod(number, 10)
           total_sum +=digit**2
         return total_sum 
     
       slow_runner = n
       fast_runner = get_sum(n)
       while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_sum(slow_runner)
        fast_runner = get_sum(get_sum(fast_runner))
       return fast_runner ==1
        
    