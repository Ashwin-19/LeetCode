class Solution {
public:
    int numTrees(int n) {
        
        vector<int> dp;
        
        for(int i = 0; i < n+1; i++)
        {
            if(i<=1)
                dp.push_back(1);
            else
                dp.push_back(0);
        }
        
        for(int i = 2; i <= n; i++)
        {
            for(int j = 1; j <= i; j++)
            {
                dp[i] += dp[j-1]*dp[i-j];
            }
        }
        
        return dp[n];
    }
};