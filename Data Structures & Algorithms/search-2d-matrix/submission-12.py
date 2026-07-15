class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS,COLS = len(matrix), len(matrix[0])

        top_row = 0
        bottom_row = ROWS - 1

        while top_row <= bottom_row:

            m = (top_row + bottom_row) // 2

            if target > matrix[m][-1]:
                top_row = m + 1
            elif target < matrix[m][0]:
                bottom_row = m - 1
            else:
                break
            
        if top_row > bottom_row:
            return False
        
        mid = m
        l,r = 0, COLS - 1
        
        while l <= r:

            m = (l + r) // 2

            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True

        return False