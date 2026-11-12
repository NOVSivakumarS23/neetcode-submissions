class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0
        cur = 0
        best = 0
        levels = 0
        for i in range(len(nums)):
            print(cur)
            if i>cur+nums[cur]:
                #reset
                cur = best
                levels+=1
            if best+nums[best]<i+nums[i]: 
                best=i
            if cur+nums[cur]>=len(nums)-1:
                return levels+1
            
