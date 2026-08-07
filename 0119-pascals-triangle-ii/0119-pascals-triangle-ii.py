class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # memory 2차원 배열 생성
        memo = [[1 for j in range(i+1)] for i in range(rowIndex + 1)] # pascal triangle
        # print(memo)
        for i in range(2,rowIndex+1,1):
            for j in range(1,i,1):
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]

        return memo[rowIndex]