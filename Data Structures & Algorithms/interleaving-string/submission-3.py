class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        maintain pointers i j k for s1 s2 s3, k = i + j
        at each step

        possible scenarios
        s1[i] == s3[k] & s3[k] != s2[j], can increment i
        s1[i] != s3[k] & s3[k] == s2[j], can increment j

        both s1[i] and s2[j] != s3[k], not possible to interleave, return false
        both s1[i] and s2[j] == s3[k] 
        we try progress i + 1 first, and keep going. 
        then we can try progress j + 1 if that doesnt work 
        if both don't work, then it's not possible
        dp saves if current state (i, j) has already been checked by a previously tracked path
        """
        if len(s3) != (len(s1) + len(s2)): return False
        dp = {}
        def dfs(i , j):
            k = i + j
            if j == len(s2): return s1[i:] == s3[k:]
            if i == len(s1): return s2[j:] == s3[k:]
            if k == len(s3): return True

            if s1[i] == s3[k] and s3[k] != s2[j]:
                if (i + 1, j) not in dp: 
                    dp[(i + 1, j)] = dfs(i + 1, j)
                return dp[(i + 1, j)]

            elif s1[i] != s3[k] and s3[k] == s2[j]:
                if (i, j + 1) not in dp:
                    dp[(i, j + 1)] = dfs(i, j + 1)
                return dp[(i, j + 1)]

            elif s1[i] != s3[k] and s3[k] != s2[j]:
                return False

            elif s1[i] == s3[k] and s3[k] == s2[j]:
                if (i + 1, j) not in dp:
                    dp[(i + 1, j)] = dfs(i + 1, j)
                if (i, j + 1) not in dp:
                    dp[(i, j + 1)] = dfs(i, j + 1)

                return dp[(i, j + 1)] or dp[(i + 1, j)]

        return dfs(0, 0)