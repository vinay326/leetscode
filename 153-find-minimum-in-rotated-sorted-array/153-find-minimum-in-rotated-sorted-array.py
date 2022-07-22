class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_value = inf
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            min_value = min(min_value, nums[mid])
            if nums[mid] < nums[hi]:
                hi = mid - 1
            else:
                lo = mid + 1
        return min_value
        
                
            
        