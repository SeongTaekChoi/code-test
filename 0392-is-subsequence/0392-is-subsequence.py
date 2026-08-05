class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        
        # (n + 1) x (m + 1) 크기의 2차원 DP 배열 0으로 초기화
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    # 문자가 같으면 이전 공통 부분 수열 길이 + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # 다르면 이전 값 중 최댓값 유지
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # 최장 공통 부분 수열의 길이가 s의 길이와 일치하는지 확인
        return dp[n][m] == n