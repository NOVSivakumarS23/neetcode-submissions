class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        mega = max(nums[-1], nums[-2])
        if len(nums)==2:
            return mega
    
        i = len(nums)-3
        nums[i] += nums[i+2]
        mega = max(nums[i], mega)
        i -= 1
        while i>=0:
            nums[i] += max(nums[i+2], nums[i+3])
            mega = max(nums[i], mega)
            i -=1
        return mega
