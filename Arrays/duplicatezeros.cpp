class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        
        int i = 0;
        
        while(i < arr.size()-1)
        {
            if(arr[i]==0)
            {
                for(int j = arr.size()-2; j >= i+1; j--)
                    arr[j+1] = arr[j];
                
                arr[i+1] = 0;
                
                i += 2;
            }
            else
            {
                i++;
            }
        }
        
    }
};