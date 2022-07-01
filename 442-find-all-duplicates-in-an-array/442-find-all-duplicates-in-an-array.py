class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        start = 0
        result =[]
        while start < len(nums):
            num = nums[start]
            if nums[start]-1 != start and nums[start] != nums[num-1]:
                nums[start], nums[num-1] = nums[num-1], nums[start]
            else:
                start +=1
                
        print(nums)
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                result.append(nums[i])
        
        return result
        