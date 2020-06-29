class Solution {
public:
    int numSquares(int n) {
        
        vector<int> nums;
        
        for(int i = 0; i < n+1; i++)   
        {
            if(i<=1)
                nums.push_back(i);
            else
                nums.push_back(INT_MAX);
        }
        
        int diff;
        int high;
        
        for(int i = 1; i < n+1; i++)
        {
            high = floor(sqrt(i));
            
            for(int j = 1; j <= high; j++)
            {
                diff = i - j*j;
                nums[i] = min(nums[i],1+nums[diff]);
            }
        }
        
        return nums[n];
    }
};