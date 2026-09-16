class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        at each step
        we can construct dp[i][j] = whether or not s[i:], p[j:] can be matched 
        when we are at s[m] p[n] both "" "", then yes

        as we move back,
        we consider first
        both are characters, if s[i] != p[j], we mark dp[i][j] as false
        if both or one is ., we mark dp[i][j] as true

        however, when we encounter *, which means matches zero or more of the preceding element
        we have two choices
        skip previous a dp[i][j] = dp[i][j + 2]
        or use one or more, so we set current position to = s[j - 1], then consume the other string so dp[i][j] = dp[i + 1][j]
        """

        m = len(s)
        n = len(p)
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]

        dp[m][n] = True

        for j in range(n - 2, -1, -1):
            if p[j + 1] == "*":
                dp[m][j] = dp[m][j + 2]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if p[j] == "*": continue

                if j < n - 1 and p[j + 1] == "*":
                    skip = dp[i][j + 2]
                    match = p[j] == s[i] or p[j] == "."
                    use = match and dp[i + 1][j]
                    dp[i][j] = skip or use
                
                elif p[j] == ".":
                    dp[i][j] = dp[i + 1][j + 1]

                else:
                    dp[i][j] = s[i] == p[j] and dp[i + 1][j + 1]
        
        return dp[0][0]

    
                