class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]

            max_diff = prices[i] - min_prices
            max_profit = max(max_profit,max_diff)
        return max_profit
