class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        izq, der = 0, len(nums)-1

        while izq<=der:
            mid=(izq+der)//2
            if nums[mid]==target:
                return mid
                break
            elif nums[mid]<target:
                izq=mid+1
            elif nums[mid]>target:
                der=mid-1
        else:
            return izq