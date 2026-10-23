class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while right>(left+1):
            mid = (left+right)//2
            if nums[mid]<nums[left]:
                #left hadn side is unsorted
                right = mid
            elif nums[mid]>nums[right]:
                left = mid
            else:
                #its acctually sorted?
                return nums[0]
        return min(nums[left], nums[right])


