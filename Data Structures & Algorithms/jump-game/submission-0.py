class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dist = 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=dist:
                dist = 1
            else: dist+=1

        return dist==1