class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heapq.heappush(heap, 1)
        seen = set()
        seen.add(1)
        
        ugly_number = 1
        
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            
            for factor in [2, 3, 5]:
                new_ugly_number = ugly_number * factor
                if new_ugly_number not in seen:
                    seen.add(new_ugly_number)
                    heapq.heappush(heap, new_ugly_number)
        
        return ugly_number
