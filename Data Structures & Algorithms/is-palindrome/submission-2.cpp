class Solution {
public:
    bool isPalindrome(string s) {
        int right = s.size()-1;
        int left = 0;
        while(left<right){
            while(!isalnum(static_cast<unsigned char>(s[left]))){left++;}
            while(!isalnum(static_cast<unsigned char>(s[right]))){right--;}
            if(left>=right){break;}
            if(tolower(static_cast<unsigned char>(s[left])) != tolower(static_cast<unsigned char>(s[right]))){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
