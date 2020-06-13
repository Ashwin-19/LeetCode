class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        l = len(nums)
        
        if l == 0 or l == 1:
            return nums
        
        dp = [1 for i in range(l)]
        backtrack = [-1 for i in range(l)]
        
        for i in range(l):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[i]<dp[j]+1:
                    dp[i] = dp[j] + 1
                    backtrack[i] = j
        
        longest = max(dp)
        index = dp.index(longest)
        
        ans = []
        
        while True:
            if index == -1:
                break
            else:
                ans.append(nums[index])
                index = backtrack[index]
        
        return ans
            