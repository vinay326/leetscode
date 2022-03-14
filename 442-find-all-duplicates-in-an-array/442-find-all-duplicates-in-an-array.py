class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = {}
        ans =[]
        for i in range(len(nums)):
            if nums[i] not in result:
                result[nums[i]] =1
            else:
                result[nums[i]] +=1
                if result[nums[i]] >= 2:
                   ans.append(nums[i])
        
        return list(set(ans))
                