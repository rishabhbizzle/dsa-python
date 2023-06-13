class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curCostPrice = float("inf")

        for price in prices:
            if price < curCostPrice:
                curCostPrice = price
            else:
                if (price - curCostPrice) > profit:
                    profit = price - curCostPrice
        return profit