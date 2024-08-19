class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        steps = 0
        original_n = n
        
        i = 2
        while i * i <= n:
            while n % i == 0:
                steps += i
                n //= i
            i += 1
        
        if n > 1:
            steps += n
        
        return steps
