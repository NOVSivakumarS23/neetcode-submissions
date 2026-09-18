class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> lookup;

        for (int n:nums){
            lookup[n]++;
        }

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minHeap;
        for (const pair<const int, int>& entry : lookup) {
            int num = entry.first;   // Map key
            int freq = entry.second; // Map value
            minHeap.push(pair<int,int>(freq,num));
            if (minHeap.size() > k) {
                minHeap.pop(); // Evict the lowest frequency element
            }
        }

        // Step 4: Extract top K elements from heap
        vector<int> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }

        return result;
    }
};
