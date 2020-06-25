class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        prev = 0
        
        for num in sorted(nums):
            
            if prev == num:
                return num
            
            prev = num