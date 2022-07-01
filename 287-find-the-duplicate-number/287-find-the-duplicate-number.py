class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = -1
        for i in range(len(nums)):
            num = nums[i]
            if nums[abs(num)-1] < 0:
                dup = abs(num)
            else:
                nums[abs(num)-1] *=-1
        return dup
            
                
           