class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
         nums_count = defaultdict(int)
         for num in nums:
            nums_count[num] +=1
         count_nums = defaultdict(set)
         for key, value in nums_count.items():
                count_nums[value].add(key)
         output =[]
         for count in sorted(count_nums.keys()):
                values = count_nums[count]
                for value in sorted(values, reverse =True):
                    output += [value] * count
         return output