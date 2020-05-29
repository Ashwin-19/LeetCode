class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        
        int n = A.size();
        int flag = 0;
        
        if(n<3)
        {
            return false;
        }
        
        for(int i = 0; i < n-1; i++)
        {
            if(A[i]==A[i+1])
                return false;
            
            else if(A[i]>A[i+1] && flag==0)
            {
                if(i>=1)
                {
                    flag=1;
                }
                else
                {
                    return false;
                }
            }
            
            else if(A[i]<A[i+1] && flag==1)
                return false;
        }
        
        if(flag==1)
        {
            return true;
        }
        return false;
    }
};