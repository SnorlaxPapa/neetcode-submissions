class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        iters = (min(rows, cols) + 1) // 2
        res = []
        for i in range(iters):
            row_start = i
            row_end = rows - i
            col_start = i
            col_end = cols - i
            #top
            res.extend(matrix[row_start][col_start: col_end])
            if row_end == row_start + 1: continue
            #right
            for row in range(row_start + 1, row_end - 1):
                res.append(matrix[row][col_end - 1])
            #bottom
            for col in range(col_end - 1, col_start - 1, -1):
                res.append(matrix[row_end - 1][col])
            #left
            if col_start + 1 == col_end: continue
            for row in range(row_end - 2, row_start, -1):
                res.append(matrix[row][col_start])

        return res