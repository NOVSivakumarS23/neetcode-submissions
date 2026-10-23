class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<(right-1):
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[left]:
                #left is sorted
                if target<nums[mid] and target>=nums[left]:
                    #its inside the left
                    right = mid
                else:
                    #it must be in the right unsorted array
                    left = mid
            elif nums[mid]<nums[right]:
                #the right is sorted
                if target>nums[mid] and target<=nums[right]:
                    #its inside the right
                    left = mid
                else:
                    #it must be in the left unsorted array
                    right = mid
        if nums[left]==target: return left
        if nums[right]==target: return right
        return -1
        