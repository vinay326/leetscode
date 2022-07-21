class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        x=1
        for i in range(len(nums)):
            answer[i] =x
            x *= nums[i]
        
        x=1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= x
            x *= nums[i]
        
        return answer
            