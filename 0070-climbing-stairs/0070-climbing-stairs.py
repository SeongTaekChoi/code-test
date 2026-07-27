class Solution:
    def __init__(self):
        self.memory = [0] * 46
        self.memory[0] = 1
        self.memory[1] = 2
    def climbStairs(self, n: int) -> int:
        # 전체 경우의 수 = 처음 1계단 오른 경우 남는 경우의 수 + 처음 2계단 오른 경우 남는 경우의 수 --> 점화식
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        # 메모이제이션
        if self.memory[n] != 0:
            return self.memory[n]
        
        self.memory[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        return self.memory[n]