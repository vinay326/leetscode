from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for i in nums:
            if i in d:
                return True
            else:
                d[i] += 1
        return False
                
        