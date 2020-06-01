class Solution {
public:
    int heightChecker(vector<int>& heights) {
        
        vector<int> copy;
        int n = heights.size();
        
        for(int i = 0; i < n; i++)
            copy.push_back(heights[i]);
        
        sort(copy.begin(),copy.end());
        
        int count = 0;
        
        for(int i = 0; i < n; i++)
        {
            if(copy[i]!=heights[i])
                count++;
        }
        
        return count;
        
    }
};