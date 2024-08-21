class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            max_distance = max(max_distance, abs(current_max - global_min), abs(global_max - current_min))
            
            global_min = min(global_min, current_min)
            global_max = max(global_max, current_max)
        
        return max_distance