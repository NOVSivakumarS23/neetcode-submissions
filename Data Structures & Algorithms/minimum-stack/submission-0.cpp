class MinStack {
public:
    vector<pair<int,int>> v;
    int min = INT_MAX;

    MinStack() {
        
    }
    
    void push(int val) {
        int min = val;
        if(v.size()>0 && v[v.size()-1].second<val){
            min = v[v.size()-1].second;
        }
        v.push_back(pair<int,int>(val,min));
    }
    
    void pop() {
        v.pop_back();
    }
    
    int top() {
        return v[v.size()-1].first;
    }
    
    int getMin() {
        return v[v.size()-1].second;
    }
};
