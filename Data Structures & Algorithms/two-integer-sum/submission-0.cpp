class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> lookup;
        vector<int> v;
        int ind = 0;
        for(int i:nums){
            lookup[i] = ind;
            ind++;
        }
        ind = 0;
        for(int i:nums){
            if(lookup.contains(target-i) && lookup[target-i]!=ind){
                if(ind<=lookup[target-i]){
                    v.push_back(ind);
                    v.push_back(lookup[target-i]);
                }else{
                    v.push_back(lookup[target-i]);
                    v.push_back(ind);
                }
                return v;
            }
            ind++;
        }
        v.push_back(-1);
        v.push_back(-1);
        return v;
    }
};
