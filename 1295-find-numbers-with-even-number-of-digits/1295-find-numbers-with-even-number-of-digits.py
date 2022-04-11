class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for a in nums:
            if len(str(a)) % 2 == 0:
                count +=1
        return count
        