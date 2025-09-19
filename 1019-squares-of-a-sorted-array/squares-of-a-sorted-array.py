class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right= len(nums)-1
        lista=[]

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                lista.append(nums[left]**2)
                left+=1
            else:
                lista.append(nums[right]**2)
                right-=1
            
        lista.reverse()
        return lista