class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) -1
        result = [0] * len(nums)
        sum_result = 0
        
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left = left+1
            else:
                square = nums[right]
                right = right -1
            result[i] =  square * square
        return result
            
        