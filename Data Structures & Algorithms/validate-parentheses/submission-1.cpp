class Solution {
public:
    bool isValid(string s) {
        stack<char> stacker;
        for(char c:s){
            if(c=='(' || c=='[' || c=='{'){stacker.push(c);}
            if(c==']' || c==')' || c=='}'){
                if(stacker.size()==0){return false;}
                if(c==']' && stacker.top()=='['){stacker.pop();}
                else if(c=='}' && stacker.top()=='{'){stacker.pop();}
                else if(c==')' && stacker.top()=='('){stacker.pop();}
                else{
                    return false;
                }
            }
        }
        if(stacker.size()!=0){return false;}
        return true;
    }
};
