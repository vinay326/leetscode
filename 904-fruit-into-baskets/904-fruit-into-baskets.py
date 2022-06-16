class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start = 0
        max_length = 0
        result = {}
        for window_end in range(len(fruits)):
            fruit_type = fruits[window_end]
            if fruit_type not in result:
                result[fruit_type] =0
            result[fruit_type] +=1
            
            while len(result) > 2:
                left_fruit = fruits[window_start]
                result[left_fruit] -=1
                if result[left_fruit] == 0:
                    del result[left_fruit]
                window_start +=1
            max_length =  max(max_length , window_end - window_start + 1)
            
        return max_length
            
        