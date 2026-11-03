class Solution:

  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
      return False

    # 1. Fix the shallow copy with a list comprehension
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True

    # 2. Initialize the first column (using only s1)
    for i in range(1, len(s1) + 1):
      dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    # 3. Initialize the first row (using only s2)
    for j in range(1, len(s2) + 1):
      dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    # 4. Fill the rest of the DP table using correct string indices
    for i in range(1, len(s1) + 1):
      for j in range(1, len(s2) + 1):
        # Check if we can match using s1's current character
        if s1[i - 1] == s3[i + j - 1]:
          dp[i][j] = dp[i][j] or dp[i - 1][j]
        # Check if we can match using s2's current character
        if s2[j - 1] == s3[i + j - 1]:
          dp[i][j] = dp[i][j] or dp[i][j - 1]

    return dp[len(s1)][len(s2)]