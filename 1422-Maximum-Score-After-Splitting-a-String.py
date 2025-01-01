class Solution(object):
    def maxScore(self, s):
        ones = s.count('1')
        zeros, maxScore = 0,0 

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1 
            total = zeros + ones
            maxScore = max(maxScore, total )

        return maxScore      
        