class Solution:
    def countOdds(self, low: int, high: int) -> int:
        contador = (high - low) // 2

        if low % 2 == 1 or high % 2 == 1:
            return contador + 1
        return contador