class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        freq = {}
        
        for item in nums:
            if item not in freq:
                freq[item] = 1
            else:
                freq[item] += 1
        
        for num in freq:
            if freq[num]==1:
                return num