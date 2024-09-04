class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        direction_index = 0
        obstacle_set = set(tuple(obs) for obs in obstacles)
        max_dist_sq = 0
        
        for command in commands:
            if command == -2:
                direction_index = (direction_index + 3) % 4
            elif command == -1:
                direction_index = (direction_index + 1) % 4
            else:
                dx, dy = directions[direction_index]
                for _ in range(command):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_dist_sq = max(max_dist_sq, x * x + y * y)
                    else:
                        break
        
        return max_dist_sq
