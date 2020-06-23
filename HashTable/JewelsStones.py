class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        col = Counter(S)
        count = 0
        
        for char in J:
            count += col[char]
        
        return count