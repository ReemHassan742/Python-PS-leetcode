class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        row, col = 0, 0
        row_start, row_end = 0, m - 1
        col_start, col_end = 0, n - 1
        
        index = 0
        while row_start <= row_end and col_start <= col_end:
            if current_direction == 0:
                for col in range(col_start, col_end + 1):
                    if index < len(values):
                        matrix[row][col] = values[index]
                        index += 1
                row_start += 1
            elif current_direction == 1:
                for row in range(row_start, row_end + 1):
                    if index < len(values):
                        matrix[row][col_end] = values[index]
                        index += 1
                col_end -= 1
            elif current_direction == 2:
                for col in range(col_end, col_start - 1, -1):
                    if index < len(values):
                        matrix[row][col] = values[index]
                        index += 1
                row_end -= 1
            elif current_direction == 3:
                for row in range(row_end, row_start - 1, -1):
                    if index < len(values):
                        matrix[row][col_start] = values[index]
                        index += 1
                col_start += 1
            
            current_direction = (current_direction + 1) % 4
        
        return matrix
