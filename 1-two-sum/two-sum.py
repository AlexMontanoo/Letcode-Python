class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for numero in range(len(nums)):
            complemento=target-nums[numero]
            
            if complemento in hashmap:
                return[hashmap[complemento],numero]
            else:
                hashmap[nums[numero]]=numero
            