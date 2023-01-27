class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # n = len(prices)
        # for buy_i, buy_p in enumerate(prices):
        #     #print(buy_i, prices[n-1])
        #     profits = [prices[sell_i] - buy_p for sell_i in range(buy_i, n)]
        #     profit = max(profit, max(profits))
        # return profit
        low = prices[0]
        curr_profit = 0
        max_profit = 0
        for i in range(1, len(prices)):
            low = min(prices[i], low)
            curr_profit = prices[i] - low
            max_profit = max(max_profit, curr_profit)
        return max_profit
