#1653
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start=0
        profit=0
        for i in range(1, len(prices)):
            if prices[i]>prices[start] and i>start:
                profit+= prices[i]-prices[start]
                start=i
            else:
                start+=1
        return profit
                
                