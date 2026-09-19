class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> stacker;
        for(string& s:tokens){
            if(s=="+"){
                int result = stacker[stacker.size()-1] + stacker[stacker.size()-2];
                stacker.pop_back();
                stacker.pop_back();
                stacker.push_back(result);
            }
            else if(s=="-"){
                int result = stacker[stacker.size()-2] - stacker[stacker.size()-1];
                stacker.pop_back();
                stacker.pop_back();
                stacker.push_back(result);
            }
            else if(s=="*"){
                int result = stacker[stacker.size()-1] * stacker[stacker.size()-2];
                stacker.pop_back();
                stacker.pop_back();
                stacker.push_back(result);
            }
            else if(s=="/"){
                int result = stacker[stacker.size()-2] / stacker[stacker.size()-1];
                stacker.pop_back();
                stacker.pop_back();
                stacker.push_back(result);
            }else{
                stacker.push_back(stoi(s));
            }
        }
        return stacker[0];
    }
};
