class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        if(target<nums[0])
            return 0;
        
        int size = nums.size();
        
        if(target>nums[size-1])
            return size;
        
        int r = size-1;
        int l = 0;
        int m;
        
        while(l<=r)
        {
            m = (l+r)/2;         

            if(m>0 && m<=size-1 && nums[m-1]<target && target<nums[m])
            {
                return m;
            }
            else if(m>=0 && m<size-1 && nums[m]<target && target<nums[m+1])
            {
                return m+1;
            }
            
            if(nums[m]==target)
            {
                return m;
            }
            else if(nums[m]<target)
            {
                l = m+1;
            }
            else
            {
                r = m-1;
            }
        }
        return -1;
    }
};