class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = -1
        missing  =1
        for i in nums:
            if nums[abs(i)-1] < 0:
                dup =  abs(i)
            else:
                nums[abs(i) - 1] *=-1
                
        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1
        
        return [dup, missing]
        
        
       
        