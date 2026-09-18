class Solution {
public:
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string result = "";
        for (const string& s : strs) {
            result += to_string(s.length()) + "#" + s;
        }
        return result;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;

        while (i < s.length()) {
            // Find the delimiter '#' starting from index i
            int j = i;
            while (s[j] != '#') {
                j++;
            }

            // Extract the length prefix
            int len = stoi(s.substr(i, j - i));

            // Extract 'len' characters after the '#'
            result.push_back(s.substr(j + 1, len));

            // Move pointer past the current string content
            i = j + 1 + len;
        }

        return result;
    }
};