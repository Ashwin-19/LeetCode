class Solution {
public:
    void reverseString(vector<char>& s) {
        
        int n = s.size();
        int m = n/2;

        char temp;
        
        for(int i = 0; i < m; i++)
        {
            char temp = s[i];
            s[i] = s[n-1-i];
            s[n-1-i] = temp;
        }
    }
};