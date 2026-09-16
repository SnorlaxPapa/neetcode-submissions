class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        max_area = 0

        def search(position):
            """
            recursively search the neighbors of this position
            """
            visited.add(position)
            row, col = position

            area = 1
            neighbors = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]   

            #iterate and check our neighbors
            for neighbor in neighbors:
                new_row, new_col = row + neighbor[0], col + neighbor[1]
                if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                    if grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                        area += search((new_row, new_col))

            return area

        #sstep through grid and check valid land to find area
        for row in range(len(grid)):
            for col in range((len(grid[0]))):
                if grid[row][col] == 0 or (row, col) in visited:
                    continue
                
                area = search((row, col))
                max_area = max(max_area, area)

        return max_area