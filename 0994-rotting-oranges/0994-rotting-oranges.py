class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        position_rot = [] # 썩은 오렌지의 위치 저장 큐
        fresh_count = 0 # 건강한 오렌지 개수
        m = len(grid)
        n = len(grid[0])
        
        # 초기 순회
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    position_rot.append((i,j)) # 초기 썩은 오렌지 위치
                elif grid[i][j] == 1:
                    fresh_count += 1

        # 순회를 마친 뒤 건강한 오렌지가 하나도 없으면 즉시 0반환 후 종료
        if fresh_count == 0:
            return 0
        
        # 썩은 오렌지 좌표를 기준으로 인접한 건강한 오렌지(1)를 날짜를 추가하면서 썩은 오렌지(2)로 바꿔가기
        date = 0 # 날짜 초기화
        while len(position_rot) > 0: # 큐가 비워질때까지
            date += 1
            
            # 1분 동안 동시에 썩는 오렌지들을 묶어서 처리하기 위해, 현재 큐에 들어있는 개수만큼만 반복
            for _ in range(len(position_rot)): 
                # pop(0)을 사용하여 먼저 들어온 오렌지부터 꺼내감
                x, y = position_rot.pop(0) 
                
                # 격자 범위를 벗어나지 않는지 먼저 확인한 후 오렌지 상태 확인
                if x+1 < m and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    fresh_count -= 1
                    position_rot.append((x+1,y))
                    
                if x-1 >= 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    fresh_count -= 1
                    position_rot.append((x-1,y))
                    
                if y+1 < n and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    fresh_count -= 1
                    position_rot.append((x,y+1))
                    
                if y-1 >= 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    fresh_count -= 1
                    position_rot.append((x,y-1))
        
        # 건강한 오렌지가 남아있으면 -1 반환, 아니면 (date-1) 반환 > 다 썩고 난 뒤 한번 더 순회하므로
        if fresh_count > 0:
            return -1
        else:
            return date-1