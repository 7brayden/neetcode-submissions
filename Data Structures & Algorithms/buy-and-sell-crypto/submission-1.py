class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float('inf')
        best = 0
        for price in prices:
            if price < minVal:
                minVal = price
            if price - minVal > best:
                best = price - minVal
        return best