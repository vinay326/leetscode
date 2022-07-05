class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        k_sum = k*(k+1)//2
        nums = [*set(nums)]
        nums.sort()
        for i in range(len(nums)):
            num = nums[i]
            if num > k:
                break
            else:
                k+=1
                k_sum -= num
                k_sum +=k
        
        return k_sum
                