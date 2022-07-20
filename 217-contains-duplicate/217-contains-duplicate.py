from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for i in range(len(nums)):
            if nums[i] in result:
                return True
            result[nums[i]] = 0
        return False
            

        