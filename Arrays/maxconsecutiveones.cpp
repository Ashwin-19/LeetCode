class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        
        int curr_max = 0;
        int global_max = 0;

        for(std::vector<int>::iterator itr = nums.begin(); itr != nums.end(); ++itr)
        {
            if(*itr==1)
            {
                curr_max++;
            }
            else
            {
                if(curr_max > global_max)
                {
                    global_max=curr_max;
                }
                curr_max = 0;
            }
        }
        if(curr_max > global_max)
        {
            global_max=curr_max;
        }
        return global_max;
    }
};