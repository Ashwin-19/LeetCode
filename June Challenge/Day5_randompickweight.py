import random

class Solution:

    def __init__(self, w: List[int]):
        
        self.len = len(w)
        
        self.presum = w
        
        for i in range(1,self.len):
            self.presum[i] += self.presum[i-1]
            
        self.maxval = self.presum[-1]
        

    def pickIndex(self) -> int:
        
        weight = random.randint(1,self.maxval)
        return self.search(0,self.len-1,weight)        
    
    def search(self,l,r,weight):
        
        if l < r:
            
            m = (l+r)//2
            
            if self.presum[m] < weight:
                return self.search(m+1,r,weight)
            else:
                return self.search(l,m,weight)
        
        return l