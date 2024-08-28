class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x: int, y: int, grid: List[List[int]], visited: List[List[bool]], island_cells: List[Tuple[int, int]]):
            stack = [(x, y)]
            cells = []
            while stack:
                cx, cy = stack.pop()
                if 0 <= cx < len(grid) and 0 <= cy < len(grid[0]) and grid[cx][cy] == 1 and not visited[cx][cy]:
                    visited[cx][cy] = True
                    cells.append((cx, cy))
                    stack.extend([(cx + dx, cy + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]])
            island_cells.append(cells)
        
        def is_sub_island(island_cells: List[Tuple[int, int]]) -> bool:
            for x, y in island_cells:
                if grid1[x][y] == 0:
                    return False
            return True

        m, n = len(grid2), len(grid2[0])
        visited = [[False] * n for _ in range(m)]
        sub_island_count = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    island_cells = []
                    dfs(i, j, grid2, visited, island_cells)
                    for cells in island_cells:
                        if is_sub_island(cells):
                            sub_island_count += 1
                            break
        
        return sub_island_count
