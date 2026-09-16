from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = 0 
        rotten = deque([])

        #step through grid to find rotten and num fresh fruits
        for row in range (len(grid)):
            for col in range (len(grid[row])):
                if grid[row][col] == 1: fresh_fruits += 1
                elif grid[row][col] == 2: rotten.append((row, col, 0))
        
        print(rotten)
        if fresh_fruits == 0:
            return 0

        #iterate through our queue to find closest fresh fruits
        max_distance = float("-inf")
        neighbors = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        while rotten:
            row, col, minute = rotten.popleft()
            for neighbor in neighbors:
                new_row, new_col = row + neighbor[0], col + neighbor[1]
                if not (new_row >= 0 and new_row < len(grid)): continue
                if not (new_col >= 0 and new_col < len(grid[row])): continue
                if grid[new_row][new_col] != 1: continue
                print(new_row, new_col, minute)

                #decrement our fresh fruit counter is fresh fruit
                if grid[new_row][new_col] == 1: fresh_fruits -= 1

                #mark cell as visited with #
                grid[new_row][new_col] = "#"

                #update
                max_distance = max(max_distance, minute + 1)
                rotten.append((new_row, new_col, minute + 1))

        if fresh_fruits > 0:
            return -1

        return max_distance
