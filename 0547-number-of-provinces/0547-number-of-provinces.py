class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        node_ex = [i for i in range(len(isConnected))]
        count = 0
        
        # node_ex가 다 사라질 때까지 반복
        while len(node_ex) > 0:
            # 1. 탐색을 시작할 노드를 뽑고 리스트(큐 역할)에 삽입
            start_node = node_ex[0]
            queue = [start_node] 
            node_ex.remove(start_node)
            
            # 2. 큐가 빌 때까지 연결관계 탐색
            while queue:
                # 기본 리스트의 pop(0)을 사용하여 맨 앞의 원소를 꺼냄 (BFS 방식)
                curr = queue.pop(0) 
                
                for next_node in range(len(isConnected)):
                    # 연결되어 있고 아직 방문하지 않은(node_ex에 있는) 노드라면
                    if isConnected[curr][next_node] == 1 and next_node in node_ex:
                        queue.append(next_node)
                        node_ex.remove(next_node)
            
            # 연결된 한 무리를 다 찾았으므로 카운트 증가
            count += 1
            
        return count