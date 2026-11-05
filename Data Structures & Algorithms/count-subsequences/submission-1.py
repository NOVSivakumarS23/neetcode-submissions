class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0]*len(t)
        dp.append(1)
        lookup = {}
        for i in range(len(t)):
            if t[i] in lookup: lookup[t[i]].append(i)
            else: lookup[t[i]] = [i]
        
        for i in range(len(s)-1, -1, -1):
            if s[i] not in lookup: continue
            for j in lookup[s[i]]:
                dp[j] += dp[j+1]
        return dp[0]



        