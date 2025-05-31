class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        multi=1
        for i in str(n):
            sum+=int(i)
            multi*=int(i)
        conta=multi-sum
        return conta