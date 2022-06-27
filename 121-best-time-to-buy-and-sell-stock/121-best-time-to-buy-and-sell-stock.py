class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        buy = prices[0]
        
        for i in prices:
            buy = min(buy, i)
            sell = i            
            profit = max(profit, sell-buy)
        return profit
        
        