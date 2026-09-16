class Solution:
    def extractCols(self, board: List[List[str]]) -> List[List[str]]:
        columns = [[] for _ in range(9)]
        for column in range (0, 9):
            for row in range(0, 9):
                if board[row][column] == ".": continue
                columns[column].append(board[row][column])
        return columns

    
    def extractBoxes(self, board: List[List[str]]) -> List[List[str]]:
        boxes = [[] for _ in range(9)]
        pos = 0
        #this will extract boxes down the column, then progress to next column
        for row in range(0, 7, 3):
            for column in range(0, 7, 3):
                for i in range(0, 3):
                    for j in range(0, 3):
                        if board[row+i][column+j] == ".": continue
                        boxes[pos].append(board[row+i][column+j])
                pos+=1
        return boxes


    def checkValid(self, candidateList: List[List[str]]) -> bool:
        """
        to check for validity of the row/col/box, we can iterate over the array.
        if it is a number, we can add it to a seen hashmap. if it alr is there, we can return false
        """

        for array in candidateList:
            seen = {}
            for digit in array:
                if digit != ".":
                    if seen.get(digit) == None:
                        seen[digit] = 1
                    else:
                        return False
        
        return True



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        first to extract columns, and boxes into respective 2d arrays, before running 
        a function to check for unique values for each.
        Row extraction -> N iter, Col extraction -> N^2 iteration, Box extraction -> 3*3 = N
        Worst Case O(N) for extraction, total extracted 1d arrays = N + N + N = 3N with N elements = 3N^2 elements
        Validity check = O(N) for each row/column/box, with 3N arrays is N^2
        Time complexity O(N^2)
        """
        if self.checkValid(board) == False: return False
        if self.checkValid(self.extractCols(board)) == False: return False
        if self.checkValid(self.extractBoxes(board)) == False: return False
        
        return True
