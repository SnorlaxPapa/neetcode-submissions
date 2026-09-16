class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        given a target string t
        at any position i in string s and j in string t
        following scenarios
        s[i] == t[j]
        can either use this current i, or skip
        s[i] != t[j]
        can only skip this current i

        so given a function calculate_ways(i, j), we are calculating the number of subsequences we can form starting at position i of string s, and position j of string t

        many (i, j) are repeated, so we can memoize this in the form of dp[i][j] where dp[i][j] represents the distinct subsequences of s[i:] equal to t[j:], then we can return dp[0][0]

        base case:
        """
        n = len(s)
        m = len(t)
        dp = {}

        def dfs(i, j):
            if j == m: return 1 #used 
            if i == n: return 0 #no possible subsequences
            
            #calculate skip case
            if (i + 1, j) not in dp:
                dp[(i + 1, j)] = dfs(i + 1, j)

            #no match
            if s[i] != t[j]: 
                dp[(i, j)] = dp[(i + 1, j)]
                return dp[(i, j)]
            
            #match
            if (i + 1, j + 1) not in dp: #use current char
                dp[(i + 1, j + 1)] = dfs(i + 1, j + 1)

            dp[(i, j)] = dp[(i + 1, j + 1)] + dp[(i + 1, j)]
            return dp[(i, j)]

        dfs(0, 0)
        return dp[(0, 0)]
