class Solution:
    def __init__(self):
        self.memo = [-1] * 1000
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 초기값
        self.memo[0] = cost[0]
        self.memo[1] = cost[1]
        # 구하고자 하는 n번째 밟을 때 총 비용 = min(1칸 아래(n-1)까지 밟을 때 총 비용 + n 밟을 때 비용,2칸 아래(n-2)까지 밟을 때 총 비용 + n 밟을 때 비용)
        for i in range(2,len(cost),1):
            self.memo[i] = min(self.memo[i-1],self.memo[i-2]) + cost[i]
        
        return min(self.memo[len(cost)-1],self.memo[len(cost)-2])