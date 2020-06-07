class Solution:
    def change(self, amount: int, coins: List[int]) -> int: 
        
        l = len(coins)
        
        ans = [1 if i==0 else 0 for i in range(amount+1)]
        
        for i in range(l):
            for j in range(1,amount+1):
                if j >= coins[i]:
                    ans[j] += ans[j-coins[i]]
        
        return ans[-1]