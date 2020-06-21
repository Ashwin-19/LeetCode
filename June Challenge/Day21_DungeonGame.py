class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        m = len(dungeon)
        
        if m == 0:
            return 1
        
        n = len(dungeon[0])
        
        dp = [[None for i in range(n)] for j in range(m)]
        
        return self.paths(0,0,m,n,dungeon,dp)
        
        
    def paths(self, i, j, m, n, dungeon,dp):
        
        if dp[i][j] != None:
            return dp[i][j]
        
        elif i==m-1 and j==n-1:
            if dungeon[i][j] > 0:
                dp[i][j] = 1
                return dp[i][j]
            else:
                dp[i][j] = 1+abs(dungeon[i][j])
                return dp[i][j]
        
        elif i==m-1:
            dp[i][j] = max(1, self.paths(i,j+1,m,n,dungeon,dp)-dungeon[i][j])
            return dp[i][j]
        elif j==n-1:
            dp[i][j] = max(1, self.paths(i+1,j,m,n,dungeon,dp)-dungeon[i][j])
            return dp[i][j]
        else:
            dp[i][j] = max(1, min(self.paths(i,j+1,m,n,dungeon,dp)-dungeon[i][j], self.paths(i+1,j,m,n,dungeon,dp)-dungeon[i][j]))
            return dp[i][j]