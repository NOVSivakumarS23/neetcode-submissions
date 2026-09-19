class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> stacker;
        vector<int> result(temperatures.size(),0);
        int i = 0;
        for(int t:temperatures){
            //the rule is that it should be decreasing

            while(stacker.size()!=0 && temperatures[stacker.top()]<t){
                //pop
                result[stacker.top()] = i-stacker.top();
                stacker.pop();
            }
            stacker.push(i);
            i++;
        }
        return result;
    }
};
