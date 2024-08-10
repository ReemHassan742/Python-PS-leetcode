class Solution:
    def floodfill(self, grid, r, c, color):
        stack = [(r, c)]
        while stack:
            x, y = stack.pop()
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 0:
                continue
            grid[x][y] = color
            stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        my_grid = [[0] * (n * 3) for _ in range(n * 3)]
        color = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    my_grid[i * 3][j * 3 + 2] = -1
                    my_grid[i * 3 + 1][j * 3 + 1] = -1
                    my_grid[i * 3 + 2][j * 3] = -1
                elif grid[i][j] == "\\":
                    my_grid[i * 3][j * 3] = -1
                    my_grid[i * 3 + 1][j * 3 + 1] = -1
                    my_grid[i * 3 + 2][j * 3 + 2] = -1

        for i in range(n * 3):
            for j in range(n * 3):
                if my_grid[i][j] == 0:
                    color += 1
                    self.floodfill(my_grid, i, j, color)

        return color


        
        