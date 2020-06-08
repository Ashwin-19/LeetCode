class Solution {
public:
    bool isPowerOfTwo(int n) {
        
        int ans = __builtin_popcount(n);
        
        if(ans==1 && n > 0)
            return true;
        else
            return false;
        
    }
};