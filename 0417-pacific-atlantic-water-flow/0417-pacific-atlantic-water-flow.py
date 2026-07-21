class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 초기화(모든 위치를 큐에 넣기)
        init_pos = []
        solution = [] # 정답 리스트
        m = len(heights)
        n = len(heights[0])
        for i in range(m): # 모든 위치 큐에 추가
            for j in range(n):
                init_pos.append([i,j])
        
        # 한 위치씩 꺼내서 탐색 진행
        for k in init_pos:
            find4dir = [k] # 탐색에 이용할 큐
            mapping_water = [k] # 물이 흐르는 위치를 기록할 큐

            # 방문 여부를 기록할 Set 추가
            visited = set()
            visited.add((k[0], k[1]))
            
            while len(find4dir) > 0: # 탐색용 큐 내 요소가 모두 사라지면 끝
                # 하나의 position 주변 4방향 탐색 > 물이 갈 수 있는 방향을 mapping water에 추가
                x, y = find4dir.pop() 
                if x-1 >= 0 and heights[x][y] >= heights[x-1][y] and (x-1, y) not in visited:
                    find4dir.append([x-1,y])
                    mapping_water.append([x-1,y])
                    visited.add((x-1, y))
                if x+1 < m and heights[x][y] >= heights[x+1][y] and (x+1, y) not in visited:
                    find4dir.append([x+1,y])
                    mapping_water.append([x+1,y])
                    visited.add((x+1, y))
                if y-1 >= 0 and heights[x][y] >= heights[x][y-1] and (x, y-1) not in visited:
                    find4dir.append([x,y-1])
                    mapping_water.append([x,y-1])
                    visited.add((x, y-1))
                if y+1 < n and heights[x][y] >= heights[x][y+1] and (x, y+1) not in visited:
                    find4dir.append([x,y+1])
                    mapping_water.append([x,y+1])
                    visited.add((x, y+1))

            # mapping_water에 있는 요소 중 위치가 태평양인 지역, 대서양인 지역 추출 > 둘 다 있으면 해당 위치를 정답 리스트에 담기
            pacific = False
            atlantic = False
            for a, b in mapping_water:
                if a == 0 or b == 0: # 태평양
                    pacific = True
                if a == m-1 or b == n-1: # 대서양
                    atlantic = True
            
            if pacific == True and atlantic == True:
                solution.append(k)
        
        return solution
