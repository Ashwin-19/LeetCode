class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        ls = len(s)
        
        if ls == 0:
            return True
        
        lt = len(t)
        
        if ls > lt:
            return False
        
        j = 0
        
        for i in range(lt):
            if j<len(s) and t[i]==s[j]:
                j+=1
            
        if j == ls:
            return True
        else:
            return False