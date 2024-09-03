class Solution(object):
    def getLucky(self, s, k):
        number = ''.join(str(ord(x) - ord('a') + 1) for x in s)
        for _ in range(k):
            number = str(sum(int(digit) for digit in number))
        
        return int(number)
