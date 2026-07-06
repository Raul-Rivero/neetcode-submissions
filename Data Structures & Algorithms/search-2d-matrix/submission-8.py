class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])

        top_row = 0
        bottom_row = ROWS - 1

        while top_row <= bottom_row:
            center_row = (top_row + bottom_row) // 2

            if target > matrix[center_row][-1]:
                top_row = center_row + 1
            elif target < matrix[center_row][0]:
                bottom_row = center_row - 1
            else:
                break

        if top_row > bottom_row:
            return False

        
        l = 0
        r = COLS - 1
        center_row = (top_row + bottom_row) // 2

        while l <= r:
            midpoint = (l + r) // 2

            if target > matrix[center_row][midpoint]:
                l = midpoint + 1
            elif target < matrix[center_row][midpoint]:
                r = midpoint - 1
            else:
                return True

        return False