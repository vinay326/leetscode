class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        result = {}
        for i in range(len(nums)):
            char =  nums[i]
            if char not in result:
                result[char] = 0
            result[char] +=1
            
            if result[char] > 1:
                return char