class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Bottom up memoization with grid[i][j] representing the number of ways we can reach a specific grid
        start from grid[0][0] as 1

        since we can only go either down or right, we go from top to bottom, left to right, invariant being we can safely update grid[i][j] when we get to it as all the cells that can reach this cell have already been traversed

        at each step, we only need [i - 1][j] and [i][j - 1]
        so we only need to maintain the previous row, and the previous element value, reducing our space complexity to O(n)
        """ 



        grid = [0 for i in range(n)]
        grid[0] = 1

        for i in range(m):
            for j in range(n):
                if j - 1 >= 0:
                    grid[j] += grid[j - 1]

        return grid[n - 1]