class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:      
        
        n = len(costs)//2
        dp = [[-1 for i in range(n+1)] for j in range(n+1)]
        return self.compute(costs,dp,0,n,n)
        
    
    def compute(self, costs, dp, k, i, j):
        
        if i == 0 and j == 0:
            
            dp[i][j] = 0
            return dp[i][j]
        
        elif dp[i][j] != -1:
        
            return dp[i][j]
        
        else:
            
            if i > 0 and j == 0:
                dp[i][j] = costs[k][0] + self.compute(costs,dp,k+1,i-1,j)
                return dp[i][j]
            
            elif j > 0 and i == 0:
                dp[i][j] = costs[k][1] + self.compute(costs,dp,k+1,i,j-1)
                return dp[i][j]
            
            else:
                dp[i][j] = min(costs[k][0] + self.compute(costs,dp,k+1,i-1,j), costs[k][1] + self.compute(costs,dp,k+1,i,j-1))
                return dp[i][j]