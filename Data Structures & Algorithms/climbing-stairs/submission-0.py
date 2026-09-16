class Solution:
    def climbStairs(self, n: int) -> int:
        """
        each step i have two choices 1 or 2
        at step 1, we default as initial 1 way to get there
        at step 2, we default as 2 ways to get there
        at step 3, we either go from step 1 (1 2) or go from step 2 (1 1 1, 2 1)
        then at step 4, we can either come from step 2 (1, 1, 2, 2, 2) or step 3 

        so as we can see, each step n is the sum of the number of ways we can reach it from
        n-1 and n-2, generalize to n = n-1, n-2

        so we can use a bottom-up approach starting from level=3, to calculate all the way up   to n. O(n) time, O(1) space
        """

        levels = [1, 2]
        while len(levels) <= n:
            levels.append(levels[-1] + levels[-2])
        
        return levels[n-1]