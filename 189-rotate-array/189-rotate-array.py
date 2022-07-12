class Solution:
    
    def rotate_(self, nums,low, high):
        while low < high:
            nums[low],nums[high] = nums[high], nums[low]
            low, high = low+1, high-1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        self.rotate_(nums,0,len(nums)-1)
        self.rotate_(nums,0, k-1)
        self.rotate_(nums,k,len(nums)-1)

        
        return nums
        