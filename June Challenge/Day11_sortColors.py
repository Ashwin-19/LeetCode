class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = nums.count(0)
        b = a + nums.count(1)
        c = b + nums.count(2)
        
        for i in range(len(nums)):
            if i < a:
                nums[i] = 0
            elif i < b:
                nums[i] = 1
            else:
                nums[i] = 2