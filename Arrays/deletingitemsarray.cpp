class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        int len = 0;
        int i = 0;
        
        while(i < nums.size())
        {
            if(nums[i]==val)
            {                
                len++;
                for(int j = i; j < nums.size(); ++j)
                {
                    if(j < nums.size()-1)
                        nums[j] = nums[j+1];   
                    
                    else if(j==nums.size()-1)
                        nums[j]=val+1;
                }
            }
            else
            {
                i++;
            }
        }
        
        return (nums.size()-len);
        
    }
};