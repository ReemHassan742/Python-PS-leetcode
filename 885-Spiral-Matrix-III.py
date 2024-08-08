class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        visited = set()
        r, c = rStart, cStart
        visited.add((r, c))
        result.append([r, c])
        
        direction_idx = 0
        steps = 1
        
        while len(result) < rows * cols:
            for _ in range(2):  
                for _ in range(steps):
                    r += directions[direction_idx][0]
                    c += directions[direction_idx][1]
                    
                    if 0 <= r < rows and 0 <= c < cols:
                        if (r, c) not in visited:
                            visited.add((r, c))
                            result.append([r, c])
                
                direction_idx = (direction_idx + 1) % 4
            
            steps += 1
        
        return result