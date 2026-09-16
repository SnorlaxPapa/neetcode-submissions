class Solution:
    def resolvePosition(self, flattenIndex: int, rowNum: int, colNum: int):
        row = flattenIndex // colNum #number of rows
        col = flattenIndex - row * colNum #number of elements before it

        return (row, col)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        m * n matrix
        non-decreasing so 5 4 3 2 1
        from examples the matrixes are strictly non-decreasing even across rows
        we can 'flatten' the array and do a binary search
        in hindsight, we cannot flatten as this operation is m*n >> log (m*n)
        so the difficulty lies in how can we search this array while preserving the 2d structure

        actually, we know that each row is fixed in length and we have the number of columns,
        so this is quite achievable.

        for example
        [[1,2,4,8],[10,11,12,13],[14,20,30,40]] is 3*4
    
        for example index 11, we can resolve it to 
        row = 11 // 4 = 2 
        column = 11 - row * 4 = 11 - 8 = 3
        position [2][3]

        we can do this for middle. then proceed to do a binary search from there. 
        """

        left = 0
        rows = len(matrix)
        cols = len(matrix[0])
        right = rows * cols - 1

        #O(log (m*n))
        while left <= right:
            middle = (left + right) // 2
            middlePos = self.resolvePosition(middle, rows, cols)
            
            if matrix[middlePos[0]][middlePos[1]] < target:
                #means element is in front
                left = middle + 1
            elif matrix[middlePos[0]][middlePos[1]] > target:
                #behind
                right = middle - 1
            else:
                return True
            
        return False
        