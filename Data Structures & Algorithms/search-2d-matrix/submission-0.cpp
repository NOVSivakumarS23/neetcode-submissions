class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int h = matrix.size();
        int w = matrix[0].size();
        int left = 0;
        int right = (h*w)-1;

        while(left<=right){
            int mid = left + ((right-left)/2);
            if(getElem(mid, matrix)==target){
                return true;
            }
            if(getElem(mid, matrix)<target){
                left = mid+1;
            }
            else if(getElem(mid, matrix)>target){
                right = mid-1;
            }
        }
        return false;
    }

    int getElem(int i, vector<vector<int>>& matrix){
        int h = matrix.size();
        int w = matrix[0].size();
        int r = i/w;
        int c = i%w;
        return matrix[r][c];
    }
};
