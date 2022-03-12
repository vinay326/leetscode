class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
       ans = prices.copy()
       stack = []
       for i in range(len(prices)):
         while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                ans[idx] = prices[idx] - prices[i]
         stack.append(i)
       return ans
                
        
        