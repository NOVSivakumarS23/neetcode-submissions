class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;
        for(int i: stones){
            maxHeap.push(i);
        }

        while(maxHeap.size()>1){
            int first = maxHeap.top();
            maxHeap.pop();
            int second = maxHeap.top();
            maxHeap.pop();
            if(first>second){
                maxHeap.push(first-second);
            }
        }
        maxHeap.push(0);
        return maxHeap.top();
    }
};
