from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        bfs_queue = deque([])

        for row in range (len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    bfs_queue.append((row, col))

        while bfs_queue:
            row, col = bfs_queue.popleft()
            neighbors = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]

            for neighbor in neighbors:
                #filter for unvisited land
                new_row, new_col = row + neighbor[0], col + neighbor[1]
                if not (new_row >= 0 and new_row < len(grid)): continue
                if not (new_col >= 0 and new_col < len(grid[row])): continue
                if grid[new_row][new_col] < 2**31 - 1: continue

                #update our distance, then append it to the queue
                grid[new_row][new_col] = grid[row][col] + 1
                bfs_queue.append((new_row, new_col))
        
