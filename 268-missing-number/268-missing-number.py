class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        while start < len(nums):
            num = nums[start]
            if num != len(nums) and nums[start] != start:
                nums[start], nums[num] = nums[num], nums[start]
            else:
                start +=1
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)