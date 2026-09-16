class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dictionary = set(wordDict)

        possible = {}
        def dfs(start):
            if start == len(s):
                return True
            
            if start in possible: 
                return possible[start]

            end = start
            for end in range(start + 1, len(s) + 1):
                if s[start: end] in dictionary and dfs(end):
                    possible[start] = True
                    return True
            
            possible[start] = False
            return False

        return dfs(0)
