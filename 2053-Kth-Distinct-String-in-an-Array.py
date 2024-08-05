class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinct_strings = [s for s in arr if count[s] == 1]
        
        if k <= len(distinct_strings):
            return distinct_strings[k - 1]
        else:
            return ""
