class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0,1,2]
        
        while len(arr) <= n:
            arr.append(arr[-1] + arr[-2])
        return arr[n]
        