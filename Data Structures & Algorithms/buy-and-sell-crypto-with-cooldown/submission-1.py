class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [0]*(n+1)
        sold = [0]*(n+1)
        idle = [0]*(n+1)
        hold[0] = -prices[0]
        for i in range(1, n+1):
            hold[i] = max(hold[i-1], idle[i-1]-prices[i-1])
            sold[i] = hold[i-1] + prices[i-1]
            idle[i] = max(idle[i-1], sold[i-1])
            
            
        return max(sold[n],idle[n])