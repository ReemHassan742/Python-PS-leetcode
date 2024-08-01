class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_altitude = 0
        
        for gain_value in gain:
            current_altitude += gain_value
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        
        return max_altitude
        