class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        unido=sorted(nums1+nums2)
        indice=len(unido)//2
        salida=0
        if len(unido)%2==0:
            salida=(unido[indice]+unido[indice-1])/2
        else:
            
            salida=unido[indice]
            
        return salida