class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        
        int m = arr.size();
        
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < m; j++)
            {
                if(arr[i] == 2*arr[j] && i!=j)
                    return true;
            }
        }
        return false;
    }
};