class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        int n = nums.size();
        
        if(n > 1)
        {
            int zeros = 0;
            int index = 1;
        
            while(zeros < n && index < n)
            {
                if(nums[zeros]==0)
                {
                    if(nums[index]!=0)
                    {
                        nums[zeros] = nums[index];
                        nums[index] = 0;
                    }
                    else
                    {
                        index++;
                    }
                }
                else
                {
                    zeros++;
                    index++;
                }
            }
        }      
    }
};