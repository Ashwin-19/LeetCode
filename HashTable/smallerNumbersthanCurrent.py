class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        ranked = sorted(nums)
        hashtab = {}
        
        for i in range(len(ranked)):
            if ranked[i] not in hashtab:
                hashtab[ranked[i]] = i
        
        arr = [-1 for i in range(len(nums))]
        for i in range(len(nums)):
            arr[i] = hashtab[nums[i]]
        
        return arrs