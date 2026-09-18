class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int maxStreak = 0;

        for (int num : numSet) {
            // Only start counting if 'num' is the beginning of a sequence
            if (!numSet.count(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (numSet.count(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                maxStreak = max(maxStreak, currentStreak);
            }
        }

        return maxStreak;
    }
};