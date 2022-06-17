class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_start, x = 0,0
        result = {}
        max_length =0 
        for window_end in range(len(nums)):
            char = nums[window_end]
            if char == 1:
                x +=1
            
            if (window_end - window_start + 1 - x) > k:
                if nums[window_start] == 1:
                    x -=1
                window_start +=1
            max_length = max(max_length,window_end - window_start + 1)
            
        return max_length
                
            
        return max_length
            
            

        
            
        