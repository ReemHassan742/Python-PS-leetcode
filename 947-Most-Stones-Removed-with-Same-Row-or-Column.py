class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        from collections import defaultdict, deque

        row_map = defaultdict(list)
        col_map = defaultdict(list)
        
        for i, (x, y) in enumerate(stones):
            row_map[x].append(i)
            col_map[y].append(i)
        
        visited = set()
        
        def bfs(start):
            queue = deque([start])
            visited.add(start)
            component_size = 0
            while queue:
                node = queue.popleft()
                component_size += 1
                x, y = stones[node]
                for neighbor in row_map[x]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                for neighbor in col_map[y]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return component_size
        
        total_removed = 0
        for i in range(len(stones)):
            if i not in visited:
                component_size = bfs(i)
                total_removed += component_size - 1
        
        return total_removed
