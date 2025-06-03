class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        dic = {}

        for i in arr:
            if 2 * i in dic:
                return True
                break
            if i % 2 == 0 and i // 2 in dic:
                return True
                break
            dic[i] = True

        else:
            return False