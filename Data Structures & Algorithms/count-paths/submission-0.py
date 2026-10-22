class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*n

        for j in range(1, m):
            print(dp)
            for i in range(1, n):
                dp[i] += dp[i-1]
        return dp[-1]
