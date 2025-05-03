class Solution:
    def romanToInt(self, s: str) -> int:
        romanos = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev = 0  

        for i in reversed(s):
            actual = romanos[i] 

            if actual < prev:
                total -= actual  
            else:
                total += actual  

            prev = actual  

        return total