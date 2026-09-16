class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        we can construct a 2d matrix of (m, n) where m is len text 1 and n is len text 2
        each position is initialized to be 0, 1 if text1[i] == text2[j]

        grid[i][j] represents longest subsequence up to text1[i] text2[j]

        dp[i][j] can be represented as max(dp[i-1][j], dp[i][j-1]) + dp[i][j]
        the invariant being by the time we reach position i, j in text1 and text2 respectively,
        we would have accounted for all possible subsequences before this position and taken the longest possible one
        """

        rows = len(text1)
        cols = len(text2)

        grid = [[0 for col in range(cols)] for row in range(rows)]
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if text1[i] == text2[j]:
                    if i - 1 >= 0 and j - 1 >= 0:
                        grid[i][j] = 1 + grid[i - 1][j - 1]
                    else:
                        grid[i][j] = 1
                
                else:
                    top = 0 if i - 1 < 0 else grid[i-1][j]
                    left = 0 if j - 1 < 0 else grid[i][j-1]
                    grid[i][j] = max(top, left)      

        return grid[-1][-1]
                


