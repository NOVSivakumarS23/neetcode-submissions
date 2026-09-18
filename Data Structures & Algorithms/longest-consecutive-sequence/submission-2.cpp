class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0; // Fix 1: Handle empty array

        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (int n : nums) {
            minHeap.push(n);
        }

        int streak = 1;
        int maxStreak = 1;
        int prev = minHeap.top();
        minHeap.pop();

        while (!minHeap.empty()) {
            if (minHeap.top() == prev + 1) {
                streak++;
            } 
            else if (minHeap.top() != prev) {
                maxStreak = max(maxStreak, streak);
                streak = 1;
            }
            prev = minHeap.top();
            minHeap.pop();
        }

        return max(maxStreak, streak); // Fix 2: Check maxStreak after loop finishes
    }
};