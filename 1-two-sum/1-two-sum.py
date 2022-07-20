class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            char = nums[i]
            if (target-char) in result:
                return [i,result[target-char]]
            if char not in result:
                result[char] = i

            