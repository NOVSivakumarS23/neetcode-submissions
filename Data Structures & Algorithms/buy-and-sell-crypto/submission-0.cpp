class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        int right = 1;
        int max = INT_MIN;
        while(right<prices.size()){
            int profit = prices[right]-prices[left];
            if(profit>max){max = profit;}
            if(prices[right]<prices[left]){
                //jump left
                left=right;
            }
            right++;
        }
        if(max<0){max = 0;}
        return max;
    }
};
