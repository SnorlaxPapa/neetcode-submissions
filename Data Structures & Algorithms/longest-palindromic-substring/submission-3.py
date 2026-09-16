class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen =  0, 0
        n = len(s)

        palindrome_table = [[False] * n for _ in range(n)]
        
        for start in range(n - 1, -1, -1):
            for end in range(start, n):
                length = end - start + 1
                if s[start] != s[end]:
                    continue
                
                if length <= 3 or palindrome_table[start + 1][end - 1]:
                    palindrome_table[start][end] = True
                    if length > resLen: 
                        resIdx = start
                        resLen = length

        return s[resIdx : resIdx + resLen]



            