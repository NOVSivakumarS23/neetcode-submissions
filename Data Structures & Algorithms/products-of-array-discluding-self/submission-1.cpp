class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> front(nums.size(),1);
        for(int i = 1; i<nums.size(); i++){
            front[i] = front[i-1] * nums[i-1];
        }

        int product = 1;
        for(int i = nums.size()-1; i>=0; i--){
            int temp = nums[i];
            nums[i] = front[i]*product;
            product*=temp;
        }
        return nums;
    }
};
