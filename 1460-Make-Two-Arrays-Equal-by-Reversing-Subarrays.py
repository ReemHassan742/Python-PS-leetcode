class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len (arr):
            return False

        target.sort()
        arr.sort()

        if target == arr : 
            return True
        else :
            return False 



        