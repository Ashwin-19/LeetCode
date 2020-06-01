class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int n = nums.size();
        
        if(n==0)
            return 0;
        
        int i1 = 1;
        int i2 = 1;
        
        while(i1 < n)
        {
            if(nums[i1]!=nums[i1-1])
            {
                nums[i2] = nums[i1];
                i2++;
            }
            i1++;
        }
        
        return i2;        
    }
};