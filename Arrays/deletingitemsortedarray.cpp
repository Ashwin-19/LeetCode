class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int len = 1;
        int n = nums.size();
        int i1 = 0;
        int i2;
        
        if(n>0)
        {
            while(i1 < n-1)
            {
                if(nums[i1]>=nums[i1+1])
                {
                    i2 = i1+1;

                    while(i2<n && nums[i2]<=nums[i1])
                    {
                        i2++;
                    }

                    if(i2<n)
                    {
                        nums[i1+1] = nums[i2];
                        len++;
                    }
                    else
                    {
                        break;
                    }
                }
                else
                {
                    len++;
                }
                i1++;
            }
            return len;
        }
        else
            return 0;
    }
};