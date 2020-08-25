class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid and not grid[0]:
            return 0
        rows,cols=len(grid),len(grid[0])
        dp= [[0]*cols for _ in range(rows)]


        for i in range(rows):
            for j in range(cols):
                if i==0 and j==0:
                    dp[i][j]=grid[0][0]
                elif i==0 and j!=0:
                    dp[i][j]= dp[i][j-1]+grid[i][j]

                elif i!=0 and j==0:
                    dp[i][j]= dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j]= min(dp[i-1][j],dp[i][j-1])+grid[i][j]

        return dp[rows-1][cols-1]