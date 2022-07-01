class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        start = 0
        while start < len(nums):
            num = nums[start]
            if nums[start]-1 != start and nums[start]!= nums[num-1]:
                nums[start], nums[num-1]= nums[num-1], nums[start]
            else:
                start +=1
        
        for i in range(len(nums)):
            if i != nums[i]-1:
                result.append(i+1)
        
        
        return result
            
            