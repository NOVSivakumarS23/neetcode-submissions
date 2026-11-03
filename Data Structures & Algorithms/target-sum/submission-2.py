class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        lookup = {0:1}
        for i in range(0, len(nums)):
            newLookup = {}
            for key in lookup:
                if key+nums[i] in newLookup:
                    newLookup[key+nums[i]] += lookup[key]
                else: newLookup[key+nums[i]] = lookup[key]
                if key-nums[i] in newLookup: newLookup[key-nums[i]] += lookup[key]
                else: newLookup[key-nums[i]] = lookup[key]
            lookup = newLookup

        if target in lookup: return lookup[target]
        return 0

