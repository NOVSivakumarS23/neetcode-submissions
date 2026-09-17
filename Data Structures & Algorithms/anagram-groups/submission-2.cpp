class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;

        for (string& s : strs) {
            int count[26] = {0};
            for (char c : s) {
                count[c - 'a']++;
            }
            
            // Build a unique key, e.g., "#1#0#2..." based on character frequencies
            string key = "";
            for (int i = 0; i < 26; i++) {
                key += "#" + to_string(count[i]);
            }
            
            mp[key].push_back(s);
        }

        vector<vector<string>> result;
        for (auto& pair : mp) {
            result.push_back(move(pair.second));
        }

        return result;
    }
};