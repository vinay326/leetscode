class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 0
        while start < len(nums)-1:
            num = nums[start]
            if nums[start] -1 != start and nums[start] != nums[num-1]:
                nums[start],nums[num-1] = nums[num-1], nums[start]
            else:
                start +=1
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return nums[i]
            
                
           