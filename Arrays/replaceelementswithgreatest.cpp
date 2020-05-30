class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        
        int max = -1;
        int n = arr.size()-1;
        
        for(int i = n; i > -1; --i)
        {
            if(i==n)
            {
                max = arr[i];
                arr[i] = -1;
            }
            
            else
            {
                if(arr[i]>max)
                {
                    max = arr[i] + max;
                    arr[i] = max - arr[i];
                    max = max - arr[i];
                }
                else
                {
                    arr[i] = max;
                }
            }
        }
        
        return arr;
    }
};