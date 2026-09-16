import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        imagine as a weighted graph, find path with lowest peak to end point 

        we can use a min-heap to find the lowest reachable neighboring peak among our different possible paths. 

        When we pop the last one, our search is done
        Invariant: At every step, we greedily take the path with the lowest possible height, guaranteeing that the final path taken consists of the lowest path taken from the initial point
        we maintain a visited set on the way to avoid recomputing stale paths
        we store our data structure as (this paths peak, row, col)

        case of two different paths leading to the same node. so we should only add to visited once we have actually popped it, as then we know we have found the lowest 
        """

        neighbors = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]   
        visited = set()

        rows, cols = len(grid), len(grid[0])
        lowest_peak = [(grid[0][0], 0, 0)]


        while lowest_peak:
            height, row, col = heapq.heappop(lowest_peak)

            if (row, col) == (rows - 1, cols - 1): return height
            
            if (row, col) in visited: continue
            visited.add((row, col))

            for neighbor in neighbors:
                new_row, new_col = row + neighbor[0], col + neighbor[1]

                #invalid checks
                if new_row < 0 or new_row >= rows: continue
                if new_col < 0 or new_col >= cols: continue
                if (new_row, new_col) in visited: continue

                #once valid, add to our min heap. 
                new_max = max(height, grid[new_row][new_col])
                heapq.heappush(lowest_peak, (new_max, new_row, new_col))



