class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        logic -> any O block connected an outer O cell is considered not enclosed
        everything else is enclosed
        dfs from each outer O block, append the positions
        iterate again, change positions not in visited to X
        """

        o_edge = set()

        rows = len(board)
        cols = len(board[0])

        neighbors = [
            (0, 1), 
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        o_nodes = set()
        def search(position):
            row, col = position
            o_nodes.add(position)

            for neighbor in neighbors:
                new_row, new_col = row + neighbor[0], col + neighbor[1]

                #check validity
                if not (new_row >= 0 and new_row < rows): continue
                if not (new_col >= 0 and new_col < cols): continue
                if (new_row, new_col) in o_nodes: continue
                if board[new_row][new_col] != 'O': continue

                search((new_row, new_col))

        #get edge Os
        for row in range(rows):
            if board[row][0] == "O":
                o_edge.add((row, 0))
            if board[row][-1] == "O":
                o_edge.add((row, cols - 1))

        for col in range(cols):
            if board[0][col] == "O":
                o_edge.add((0, col))
            if board[-1][col] == "O":
                o_edge.add((rows - 1, col))
        
        #search edge Os
        for position in o_edge:
            search(position)

        for row in range(rows):
            for col in range(cols):
                if (row, col) in o_edge: continue
                if (row, col) not in o_nodes:
                    board[row][col] = "X"


