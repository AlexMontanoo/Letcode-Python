# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        izq=1
        der=n
        while izq<der:
            mid=(izq+der)//2
            if isBadVersion(mid):
                der=mid
            else:
                izq=mid+1
        return izq