class Solution(object):
    def stringMatching(self, words):

        arr=" ".join(words)

        subString = [word for word in words if arr.count(word)>1]

        return subString