class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for p in range(len(nums)):
            char = nums[p]
            if (target - char)  in result:
                return [result[target-char], p]
            if char not in result:
                result[char] = p

        