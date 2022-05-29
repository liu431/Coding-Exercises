class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left, max_diff = 0, 0
        for ind, price in enumerate(prices):
            # Update the minimal value to the left of the current value
            if price < prices[min_left]:
                min_left = ind
            # Update the current max difference
            max_diff = max(max_diff, price - prices[min_left])
        return max_diff
