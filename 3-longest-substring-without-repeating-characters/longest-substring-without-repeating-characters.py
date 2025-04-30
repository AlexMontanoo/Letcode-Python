class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        izq = 0
        conjunto = set()
        maximo = 0

        for der in range(len(s)):
            while s[der] in conjunto:
                conjunto.remove(s[izq])
                izq += 1

            conjunto.add(s[der])
            maximo = max(maximo, der - izq + 1)

        return maximo