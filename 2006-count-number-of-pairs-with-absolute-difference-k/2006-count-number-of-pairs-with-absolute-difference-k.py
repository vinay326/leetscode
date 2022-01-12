class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = defaultdict(int)
        h[nums[0]] += 1
        
        res = 0 
        for i in range(1, n):
            res += h[nums[i]+k] + h[nums[i]-k]
            h[nums[i]] += 1
        
        print(h)
        return res
            