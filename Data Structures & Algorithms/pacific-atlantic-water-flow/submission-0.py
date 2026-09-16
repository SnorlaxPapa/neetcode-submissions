class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        multi source dfs involving the edge of the board 
        """
        
        results = []
        neighbors = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        #set up my pacific and atlantic nodes
        pacific_nodes = set()
        atlantic_nodes = set()

        num_rows = len(heights)
        num_cols = len(heights[0])

        for i in range(num_cols):
            pacific_nodes.add((0, i))
            atlantic_nodes.add((num_rows - 1, i))
        
        for i in range(num_rows):
            pacific_nodes.add((i, 0))
            atlantic_nodes.add((i, num_cols - 1))

        print(pacific_nodes, atlantic_nodes)
        #a recursive fn that searches unvisited neighbors
        def dfs(original, index, visited):
            row, col = index
            original.add(index)
            visited.add(index)

            for neighbor in neighbors:
                new_row, new_col = row + neighbor[0], col + neighbor[1]

                if not (new_row >= 0 and new_row < num_rows): continue
                if not (new_col >= 0 and new_col < num_cols): continue
                if (new_row, new_col) in visited: continue
                if heights[new_row][new_col] < heights[row][col]: continue

                dfs(original, (new_row, new_col), visited)

        pacific_reachable = set()
        for node in pacific_nodes:
            dfs(pacific_reachable, node, set())

        atlantic_reachable = set()
        for node in atlantic_nodes:
            dfs(atlantic_reachable, node, set())


        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    results.append([row, col])

        return results

