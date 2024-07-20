class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        matrix = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                value = min(rowSum[i], colSum[j])
                matrix[i][j] = value
                
                rowSum[i] -= value
                colSum[j] -= value
        
        return matrix
