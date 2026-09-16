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

        dp = {}
        def dfs(buying, day, profit):
            if day >= len(prices):
                return 0
            if (buying, day) in dp: return dp[(buying, day)]
            
            #if we have no coin, two choices: buy today, or skip today
            if buying:
                profit_choice = dfs(False, day + 1, profit) - prices[day]
                profit_skip = dfs(True, day + 1, profit)
            #if we have coin, two choices: sell today, or skip today
            if not buying:
                profit_choice = dfs(True, day + 2, profit) + prices[day]
                profit_skip = dfs(False, day + 1, profit)

            max_profit = max(profit_choice, profit_skip)
            dp[(buying, day)] = max_profit
            
            return dp[(buying, day)]

        return dfs(True, 0, 0)





