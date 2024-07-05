class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range (min (len(word1) , len(word2))):

            result += word1 [i]
            result += word2 [i]

        if len (word1) > len (word2) :
            result += word1[ i+1 :  ]
        else :
            result += word2 [ i+1 : ]    


        return result 












