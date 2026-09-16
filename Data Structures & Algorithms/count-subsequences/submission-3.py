class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [0 for i in range(n + 1)]
        dp[n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(0, n):
                if s[i] == t[j]:
                    dp[j] += dp[j + 1]

        return dp[0]