class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> front;
        int product = 1;
        for(int n:nums){
            front.push_back(product);
            product*=n;
        }

        product = 1;
        for(int i = nums.size()-1; i>=0; i--){
            int temp = nums[i];
            nums[i] = front[i]*product;
            product*=temp;
        }
        return nums;
    }
};
