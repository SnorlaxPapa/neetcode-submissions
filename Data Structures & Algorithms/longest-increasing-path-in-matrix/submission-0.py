class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        At each position:
        we have the following options (if valid)
        go up, go left, go right, go down (4)

        a brute force operation would be to dfs every single possible valid path for an exponentially increasing solution in time and space.

        instead, we can cache already visited states. in a path, we need not care about nodes we have alr visited as the only valid path is strictly increasing, and therefore it is not possible to form a cycle through dfs, where dp[i][j] represents the longest increasing path from node (i, j)

        then, we simply find the greatest dp[i][j] in the array

        this way of memoization would require O(mn) space for mn different grids (m = rows, n = cols)
        with O(nm) time as we cache each node
        """
        rows = len(matrix)
        cols = len(matrix[0])
        dp = {}

        neighbors = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        def dfs(row, col):
            """find longest path starting from (row, col)"""
            max_path = 1
            if (row, col) in dp: return dp[(row, col)]

            for neighbor in neighbors:
                new_row, new_col = row + neighbor[0], col + neighbor[1]
                if new_row < 0 or new_row >= rows: continue
                if new_col < 0 or new_col >= cols: continue
                if matrix[new_row][new_col] <= matrix[row][col]: continue

                max_path = max(max_path, 1 + dfs(new_row, new_col))

            dp[(row, col)] = max_path
            return dp[(row, col)] 

        max_path = 1
        for row in range(rows):
            for col in range(cols):
                max_path = max(max_path, dfs(row, col))
        
        return max_path
        

