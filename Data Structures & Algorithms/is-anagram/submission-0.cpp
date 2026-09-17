class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size()){return false;}
        int lookup[26] = {0};
        for(char c:s){
            lookup[c-'a'] -= 1;
        }
        for(char c:t){
            lookup[c-'a'] += 1;
        }
        for(int i:lookup){
            if(i!=0){return false;}
        }
        return true;

    }
};
