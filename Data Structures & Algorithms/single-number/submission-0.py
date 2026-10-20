class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lookup = 0
        for num in nums:
            lookup = lookup ^ num
        return lookup