class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mega = 1
        dp = [1]*len(nums)
        i = len(nums)-2
        while i>=0:
            j = i+1
            add = 0
            while j<len(nums):
                if nums[j]>nums[i] and dp[j]>add:
                    add = dp[j]
                j+=1
            dp[i] += add
            mega = max(mega, dp[i])
            i-=1
        return mega