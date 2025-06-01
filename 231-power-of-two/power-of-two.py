class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return False
        bina=bin(n)[2:].count('1')
        if bina==1:
            return True
        else:
            return False
        
        
        