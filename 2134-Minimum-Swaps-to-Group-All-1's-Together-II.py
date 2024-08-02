class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        countOnes = sum(nums)
        
        if countOnes <= 1:
            return 0
        
        n = len(nums)
        minZeros = float('inf')
        
        nums *= 2
        
        window_size = countOnes
        current_zeros = sum(1 for i in range(window_size) if nums[i] == 0)
        minZeros = current_zeros
        
        for i in range(1, n):
            current_zeros = current_zeros - (nums[i - 1] == 0) + (nums[i + window_size - 1] == 0)
            minZeros = min(minZeros, current_zeros)
        
        return minZeros
