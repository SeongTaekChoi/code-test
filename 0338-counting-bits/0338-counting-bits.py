class Solution:
    def __init__(self):
        self.dp = [-1] * 100000
        self.ans = [0,1]
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        # 짝수는 2로 나누었을 떄 값과 1 개수 동일
        # 짝수 계산 후 홀수는 이전 짝수의 1개수에 +1만하면 됨
        self.dp[0] = 0
        self.dp[1] = 1
        for i in range(2, n+1, 1):
            if i % 2 == 0: # 짝수일 때
                self.dp[i] = self.dp[i//2]
                self.ans.append(self.dp[i])
            else: # 홀수일 때
                self.dp[i] = self.dp[i-1] + 1
                self.ans.append(self.dp[i])

        return self.ans