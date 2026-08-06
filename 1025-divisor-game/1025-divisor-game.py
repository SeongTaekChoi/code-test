class Solution:
    def divisorGame(self, n: int) -> bool:
        # 앨리스의 승리/패배를 메모리에 저장해나감
        # 초기화
        dp = [False] * 1001

        # 2부터 n까지 승패 여부 계산
        for i in range(2, n+1):
            for x in range(1, i):
                if i % x == 0: # 약수를 모두 탐색
                    if not dp[i-x]: # 끝까지 돌려서도 0이 아니면 True
                        dp[i] = True
                        break
        return dp[n]