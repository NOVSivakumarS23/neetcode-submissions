class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int n = 0;
        for(int i:piles){n+=i;}
        int left = 1;
        int right = *max_element(piles.begin(), piles.end());

        int min = right;

        while(left<=right){
            int mid = left + ((right-left)/2);
            if(calcHours(piles, mid)>h){
                left = mid+1;
            }
            if(calcHours(piles,mid)<=h){
                min = mid;
                right = mid-1;
            }
        }
        return min;
    }

    int calcHours(vector<int>& piles, int speed){
        int hours = 0;
        for(int i:piles){
            hours += i/speed;
            if(i==0){
                hours++;
            }else if(i%speed!=0){
                hours++;
            }
        }
        return hours;
    }
};
