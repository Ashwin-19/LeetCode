class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        counted = Counter(A)
        
        for key in counted:
            if counted[key] > 1:
                return key
        
        return -1