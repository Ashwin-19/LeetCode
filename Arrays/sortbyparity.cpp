class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        
        int n = A.size();
        int p1 = 0;
        int p2 = 1;
        
        while(p1 < n && p2 < n)
        {
            if(A[p1]%2!=0)
            {
                if(A[p2]%2==0)
                {
                    A[p1] = A[p1] + A[p2];
                    A[p2] = A[p1] - A[p2];
                    A[p1] = A[p1] - A[p2];
                }
                else
                {
                    p2++;
                }
            }
            else
            {
                p1++;
                p2++;
            }
        }
        
        return A;
    }
};