class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])

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

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[center_row][mid]:
                l = mid + 1
            elif target < matrix[center_row][mid]:
                r = mid - 1
            else:
                break
        
        return matrix[center_row][mid] == target