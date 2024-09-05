class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_rolls = n + m
        total_sum = mean * total_rolls
        observed_sum = sum(rolls)
        missing_sum = total_sum - observed_sum
        
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        result = [1] * n
        remaining_sum = missing_sum - n
        
        for i in range(n):
            add = min(5, remaining_sum)
            result[i] += add
            remaining_sum -= add
        
        return result
