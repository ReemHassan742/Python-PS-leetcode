from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        result = []
        for i in range(m):
            start_index = i * n
            end_index = start_index + n
            result.append(original[start_index:end_index])
        
        return result
