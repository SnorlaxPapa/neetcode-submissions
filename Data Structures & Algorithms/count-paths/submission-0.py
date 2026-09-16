class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Bottom up memoization with grid[i][j] representing the number of ways we can reach a specific grid
        start from grid[0][0] as 1

        since we can only go either down or right, we go from top to bottom, left to right, invariant being we can safely update grid[i][j] when we get to it as all the cells that can reach this cell have already been traversed
        """ 



        grid = [[0 for i in range(n)] for i in range(m)]
        grid[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i - 1 >= 0: 
                    grid[i][j] += grid[i -1][j]
                if j - 1 >= 0:
                    grid[i][j] += grid[i][j - 1]

        return grid[m - 1][n - 1]