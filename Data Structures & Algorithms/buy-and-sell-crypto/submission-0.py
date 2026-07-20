class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        summ = 0
        for r in range(len(prices)):
            if prices[l]>prices[r]:
                l+=1
            summ = max(summ, prices[r]-prices[l])
        
        return summ
