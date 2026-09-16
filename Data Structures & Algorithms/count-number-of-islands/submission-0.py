class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        find groups of 1s within a grid
        can maintain a visited set for visited islands

        iterate through the board 
        continue if val == 0
        if our value = 1, we check if alr in visited islands

        if not, we run a recursive dfs search in all directions for its neighboring 1s
        once all directions done, we add 1 to the count and move to the next one
        """

        visited = set()
        count = 0
        neighbors = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        def search(index):
            #given an index, we check its neighbors if they're 1s and haven't been visited
            row, col = index
            visited.add(index)
            #check if neighbor within confine, and if is land block yet to be visited
            for neighbor in neighbors:
                new_row = row + neighbor[0]
                new_col = col + neighbor[1]
                #if valid, check if unvisited land and launch recursive search
                if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                    if grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                        search((new_row, new_col))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "0": continue
                if (row, col) in visited: continue

                search((row, col))
                count += 1
        
        return count

