class Solution(object):
    def vowelStrings(self, words, queries):
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        words_truth = [0] * (n + 1)  
        count = 0
        
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            words_truth[i + 1] = count  
        
        result = []
        for query in queries:
            result.append(words_truth[query[1] + 1] - words_truth[query[0]])
        
        return result