class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 리스트 요소가 하나씩 추가될 때 이전 리스트 동일 인덱스 요소 + 이전 요소?
        # 파스칼의 삼각형 메모리 생성
        memo = [[1 for j in range(i+1)] for i in range(numRows)]
        # print(memo)
        # 점화식
        for i in range(2, numRows,1):
            for j in range(1,i,1):
                    memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

        return memo