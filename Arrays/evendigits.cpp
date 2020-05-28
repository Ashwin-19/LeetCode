#include<string>  

class Solution {
public:
    int findNumbers(vector<int>& nums) 
    {
        int count = 0;
        
        for(std::vector<int>::iterator itr = nums.begin(); itr != nums.end(); ++itr)
        {
            string str = to_string(*itr);
            if(str.length()%2==0)
            {
                count++;
            }
        }
        return count;
    }
};