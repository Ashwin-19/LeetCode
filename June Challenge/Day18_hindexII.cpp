class Solution {
public:
    int hIndex(vector<int>& citations) {
        
        int l, r, m, size;
        
        size = citations.size();
        
        if(size==0)
            return 0;
        
        l = 0;
        r = size-1;
        
        while(l<=r)
        {
            m = (l+r)/2;
            
            if(citations[m]==citations.size()-m)
                return citations[m];
            
            if(citations[m]<citations.size()-m)
                l = m+1;
            else
                r = m-1;
        }
        
        return size-l;
    }
};