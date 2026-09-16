class Solution:
    def countSubstrings(self, s: str) -> int:

        counter = 0

        def expand(left, right):
            if right >= len(s): return

            if s[left] == s[right]:
                nonlocal counter
                counter += 1

                if left - 1 >= 0 and right + 1 < len(s):
                    expand(left - 1, right + 1)

        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)

        return counter