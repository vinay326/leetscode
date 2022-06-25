class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = -1
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                dup = abs(nums[i])
            else:
                nums[abs(nums[i])-1] *=-1
        return dup
                
           