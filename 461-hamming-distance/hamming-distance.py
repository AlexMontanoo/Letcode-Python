class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        contador=bin(x^y).count('1')
        return contador