class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins = [min(row) for row in matrix]
        
        transpose_matrix = list(zip(*matrix))
        col_maxs = [max(col) for col in transpose_matrix]
        
        lucky_nums = [num for num in row_mins if num in col_maxs]
        
        return lucky_nums
