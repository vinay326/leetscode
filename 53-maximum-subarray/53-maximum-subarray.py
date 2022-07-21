class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum , curr_sum = nums[0], 0
        for i in nums:
            if curr_sum < i and curr_sum < 0:
                curr_sum =i
            else:
                curr_sum +=i
            max_sum = max(curr_sum, max_sum)
        
        return max_sum