class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        okay given index (i, j)
        i have following choices at each char word1[i]
        1) insert a character insert word2[j]
        2) delete the character
        3) replace word1[i] with word2[j]

        intuitively
        when word1[i] == word2[j]:
        we do not want to do anything to word1

 
        when word1[i] != word2[j]:
        1) we can replace word1[i] with word2[j] and our next state is (i + 1, j + 1)
        2) we can insert word2[j] here and our next state is (i, j + 1), meaning we insert, go next is still word1[i], with new word2 target char
        3) we can delete word1[i] and carry on, so our next state is (i + 1, j) as non-matching

        then dp[(i, j)] represents minimum number of transformations needed from word1[i:] to word2[j: ]

        we can fill dp[i][j] from the bottom up as well
        for 
        m = len(word1) and n = len(word2)

        then at each step,
        if the characters match, then dp[i][j] = dp[i + 1][j + 1]
        if not
        then dp[i][j] = min(dp[i][j + 1] insert, dp[i+1][j + 1] replace, dp[i + 1][j] delete)

        then we can return dp[0][0]
        we observe that we only need the i + 1th array, so we can optimize space to O(m) by only preserving the previous array, and working from left to right for word2.
        """

        m = len(word1)
        n = len(word2)

        dp = [n - j for j in range(n + 1)] #start by representing i = m 
        
        for i in range(m - 1, -1, -1):
            prev_diag = dp[n]
            dp[n] = m - i 
            
            for j in range(n - 1, -1, -1):
                old_diag = dp[j]

                if word1[i] == word2[j]:
                    dp[j] = prev_diag
                
                else:
                    dp[j] = 1 + min(prev_diag, dp[j + 1], dp[j])
                
                prev_diag = old_diag

        return dp[0]



