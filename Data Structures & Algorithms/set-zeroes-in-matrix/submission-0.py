class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        def replaceRow(row):
            for col in range(cols):
                if matrix[row][col] == 0: continue
                matrix[row][col] = "zero"

        def replaceCol(col):
            for row in range(rows):
                if matrix[row][col] == 0: continue
                matrix[row][col] = 0

        #rows       
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    replaceRow(row)
                    break
        
        for col in range(cols):
            for row in range(rows):
                if matrix[row][col] == 0:
                    replaceCol(col)
                    break
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "zero":
                    matrix[row][col] = 0        


        
        