class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i=0
        for num in nums:
            n ^= num^i
            i+=1
        return n