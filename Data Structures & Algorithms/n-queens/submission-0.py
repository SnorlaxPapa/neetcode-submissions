class Solution:
    def checkValid():
        pass

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1: return [["Q"]]

        board = [["." for i in range(n)] for j in range (n)]
        results = []

        #recursive backtracking function that checks validity of position before inserting queen
        def search(
            board, 
            row, 
            col_occupied, 
            diag_up_occupied, 
            diag_down_occupied, 
            ):
            #return if row matches n, means all queens put down
            if row == n:
                results.append(["".join(row) for row in board])
            
            #we try all positions in each row
            for col in range(n):
                if col in col_occupied: continue

                #calculate our up and down diags and check if theyre occupied
                up_diag = row + col
                down_diag = row - col

                if up_diag in diag_up_occupied: continue
                if down_diag in diag_down_occupied: continue

                #all 3 valid, add occupancy and recursively call alg
                board[row][col] = "Q"
                col_occupied.add(col)
                diag_up_occupied.add(up_diag)
                diag_down_occupied.add(down_diag)

                search(
                    board,
                    row+1, 
                    col_occupied,
                    diag_up_occupied,
                    diag_down_occupied
                )

                #reset
                board[row][col] = "."
                col_occupied.discard(col)
                diag_up_occupied.discard(up_diag)
                diag_down_occupied.discard(down_diag)
        
        search(
            board,
            0,
            set(),
            set(),
            set()
        )

        return results

