class Solution {
public:
    string getPermutation(int n, int k) {
        
        vector<int> seq;
        
        for(int i = 0; i < n; i++)
            seq.push_back(i+1);
        
        for(int i = 1; i < k; i++)
        {
            next_permutation(seq.begin(),seq.end());
        }
        
        string s = "";
        
        for(int i = 0; i < n; i++)
            s += to_string(seq[i]);
        
        return s;
        
    }
};