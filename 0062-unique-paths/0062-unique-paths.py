class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 점화식: 현재 칸까지의 전체 경우의 수 = 위 칸까지의 전체 경우의 수 + 왼쪽 칸까지의 전체 경우의 수
        # 메모이제이션
        memo = [[0 for j in range(n)] for i in range(m)]
        # 초기화
        for k in range(n):
            memo[0][k] = 1
        for l in range(m): 
            memo[l][0] = 1
        # 점화식
        for i in range(1,m,1):
            for j in range(1,n,1):
                memo[i][j] = memo[i-1][j] + memo[i][j-1]

        return memo[m-1][n-1]
