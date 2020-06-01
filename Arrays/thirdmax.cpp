class Solution {
public:
    int thirdMax(vector<int>& nums) {
        
        int n = nums.size();
        
        int m1 = nums[0];
        int m2 = INT_MIN;
        int m3 = INT_MIN;
        
        int f2 = 0;
        int f3 = 0;
        
        for(int i = 0; i < n; i++)
        {
            if(nums[i]>m1)
            {
                m3 = m2;
                m2 = m1;
                m1 = nums[i];
            }
            else if(nums[i]>m2 && nums[i]<m1)
            {
                m3 = m2;
                m2 = nums[i];
            }
            else if(nums[i]>m3 && nums[i]<m2 && nums[i]<m1)
            {
                m3 = nums[i];
            }
            
            if(nums[i]==m2)
            {
                f2 = 1;
            }
            if(nums[i]==m3)
            {
                f3 = 1;
            }
        }
        
        if(n<3)
            return m1;
        
        if((m2==INT_MIN && f2==0)|(m3==INT_MIN && f3==0)|m2==m3)
            return m1;
        else
            return m3;
            
    }
};