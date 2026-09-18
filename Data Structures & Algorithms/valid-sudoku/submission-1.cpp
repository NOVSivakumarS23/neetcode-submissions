class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int lookup[9] = {0};

        for(int i = 0; i<board.size(); i++){
            for(int j = 0; j<board.size(); j++){
                if (board[i][j] == '.') continue;
                int b = ((i/3)*3) + (j/3);
                int val = board[i][j] - '1';
                int mask = (1 << i) | (1 << (j + 9)) | (1 << (b + 18));
                if(lookup[val] & mask){
                    return false;
                }
                lookup[val] = lookup[val] | mask;
            }
        }
        return true;
    }
};
