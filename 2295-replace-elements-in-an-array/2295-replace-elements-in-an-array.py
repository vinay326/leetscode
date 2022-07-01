class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        result = {}
        for i in range(len(nums)):
            result[nums[i]] = i
        for i in range(len(operations)):
            num = operations[i][0]
            if num in result:
                nums[result[num]] = operations[i][1]
                result[operations[i][1]] = result[num]
                del result[num]
        return nums 
        