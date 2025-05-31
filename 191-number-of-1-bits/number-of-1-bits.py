class Solution:
    def hammingWeight(self, n: int) -> int:
        contador=bin(n).count('1')
        return contador