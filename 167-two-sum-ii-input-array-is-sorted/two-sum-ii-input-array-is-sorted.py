class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numeros=[]

        left, right = 0, len(numbers)-1

        while left<=right:
            if (numbers[left]+numbers[right]) < target:
                left+=1
            elif (numbers[left]+numbers[right]) > target:
                right-=1
            else:
                numeros.append(left+1)
                numeros.append(right+1)
                break
        return numeros