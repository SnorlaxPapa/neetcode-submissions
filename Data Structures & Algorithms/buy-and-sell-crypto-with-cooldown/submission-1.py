class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        at each step, we have the following states:
        no coin
        have coin

        if we have no coin, we make the following decisions:
        buy, no buy

        if we have coin, we make the following decisions
        sell, no sell

        we can maintain two separate arrays buy and sell
        buy[i] represents the greatest profit we can get when not holding onto a coin on day i
        sell[i] represents the greatest profit we can get when holding onto a coin on day i

        or we can simplify this to a basic state buying with key (buying, i)
        """
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)] #0 for buy, 1 for sell
        for i in range(n - 1, -1, -1):
            #account for buying
            buy = dp[i + 1][1] - prices[i] #buy today
            skip = dp[i + 1][0] #sell today

            dp[i][0] = max(buy, skip)

            #selling
            sell = dp[i + 2][0] + prices[i] if i + 2 < n else prices[i]
            skip = dp[i + 1][1] 
            dp[i][1] = max(sell, skip)
        
        return dp[0][0]








