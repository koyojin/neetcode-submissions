#1716-
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for start in range(len(prices)-1):
            for end in range(len(prices)):
                if end>0 and prices[end]>prices[start] and end>start:
                    profit=max(profit, prices[end]-prices[start])
                    print(prices[end],prices[start])
        return profit