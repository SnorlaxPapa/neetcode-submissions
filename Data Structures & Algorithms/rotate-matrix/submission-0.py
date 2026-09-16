class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        def rotate_cell(pos: tuple[int], curr_value: int, root: tuple[int], is_start: bool):
            if pos == root and not is_start:
                return
            
            row, col = pos 
            next_row = col
            next_col = n - 1 - row

            next_value = matrix[next_row][next_col]
            matrix[next_row][next_col] = curr_value

            rotate_cell((next_row, next_col), next_value, root, False)


        for row in range(n // 2):
            for col in range((n + 1) // 2):
                rotate_cell(
                    (row, col),
                    matrix[row][col],
                    (row, col),
                    True
                )

