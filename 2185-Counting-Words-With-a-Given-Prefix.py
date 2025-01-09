class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        counter = 0
        l = len(pref)
        for word in words:
            if len(word) >= l and word[:l] == pref:
                counter += 1
        return counter