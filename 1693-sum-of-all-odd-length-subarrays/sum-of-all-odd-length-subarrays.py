class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=0
        n = len(arr)

        for i in range(n):
            total_subarrays = (i + 1) * (n - i)
            odd_subarrays = (total_subarrays + 1) // 2
            total += arr[i] * odd_subarrays

        return total