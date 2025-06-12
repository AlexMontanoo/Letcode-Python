class Solution:
    def numberOfSteps(self, num: int) -> int:
        contador=0
        while num != 0:
            if num%2==0:
                num=num/2
            elif num%2==1:
                num=num-1
            contador+=1
        return contador