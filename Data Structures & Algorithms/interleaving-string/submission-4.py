class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        dp = [False for i in range(n + 1)]
        if len(s3) != m + n: return False
        dp[n] = True

        for i in range(m, -1, - 1):
            for j in range(n, -1, -1):
                if i == m and j == n: continue
                k = i + j
                curr = False
                if i < m and s1[i] == s3[k]:
                    curr |= dp[j]
                if j < n and s2[j] == s3[k]:
                    curr |= dp[j + 1]
                dp[j] = curr
        return dp[0]
