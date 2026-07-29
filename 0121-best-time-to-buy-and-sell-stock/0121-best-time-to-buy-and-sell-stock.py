class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 주식 가격 데이터가 없으면 이익을 낼 수 없으므로 0을 반환합니다.
        if not prices:
            return 0

        # 지금까지 지나온 날들 중 가장 낮았던 주식 가격 (초기값은 무한대)
        min_price = float(10001)
        
        # max_profit: 현재까지 얻을 수 있는 최대 이익 (초기값은 0)
        max_profit = 0
        
        # 배열을 왼쪽에서 오른쪽으로 딱 한 번만 순회합니다.
        for price in prices:
            # 1. 최저점 갱신 (점화식: M[i] = min(M[i-1], P[i]))
            # 어제까지의 최저점(min_price)과 오늘 가격(price) 중 더 작은 값으로 갱신
            min_price = min(min_price, price)
            
            # 2. 최대 이익 갱신 (점화식: DP[i] = max(DP[i-1], P[i] - M[i]))
            # 어제까지의 최대 이익(max_profit)과 오늘 가격에서 최저점을 뺀 이익(price - min_price) 중 더 큰 값으로 갱신
            max_profit = max(max_profit, price - min_price)
            
        # 순회가 끝나면 계산된 최종 최대 이익을 반환합니다.
        return max_profit