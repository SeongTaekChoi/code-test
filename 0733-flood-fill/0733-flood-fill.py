class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        # 초기 영역 색상 확인
        init_color =  image[sr][sc]
        color_queue = [[sr,sc]] # 주변 탐색을 위한 큐
        
        # 영역의 색깔 전체가 color와 같으면, 그대로 출력
        if init_color == color:
            return image
            
        # 시작 픽셀의 색상을 미리 변경
        image[sr][sc] = color 
        
        # 초기 위치부터 주변 초기 색상과 동일 색상이 없어질 때까지 수행
        while len(color_queue) > 0:
            x, y = color_queue.pop()
            # 주변 색상이 init_color와 동일한지 확인
            if x+1 < m and image[x+1][y] == init_color:
                image[x+1][y] = color
                color_queue.append([x+1,y])
            if x-1 >= 0 and image[x-1][y] == init_color:
                image[x-1][y] = color
                color_queue.append([x-1,y])
            if y+1 < n and image[x][y+1] == init_color:
                image[x][y+1] = color
                color_queue.append([x,y+1])
            if y-1 >= 0 and image[x][y-1] == init_color:
                image[x][y-1] = color
                color_queue.append([x,y-1])

        return image