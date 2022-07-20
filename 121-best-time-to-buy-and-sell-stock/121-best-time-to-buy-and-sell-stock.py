class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        n = len(prices)
        i=0
        j=i+1
        while j <= n-1:
            if prices[i] > prices[j]:
                i = j
                j = i+1
            else:
                max_sum = max(max_sum, prices[j] - prices[i])
                j+=1
        return max_sum
            
        