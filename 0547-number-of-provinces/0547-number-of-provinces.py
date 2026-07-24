from typing import List
import collections

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # node_all은 사용하지 않아도 되므로 생략했습니다.
        node_ex = [i for i in range(len(isConnected))]
        count = 0
        
        # node_ex가 다 사라질 때까지 반복
        while len(node_ex) > 0:
            # 1. 탐색을 시작할 노드를 하나 뽑아 큐에 넣고, node_ex에서 제거(방문 처리)
            start_node = node_ex[0]
            queue = collections.deque([start_node])
            node_ex.remove(start_node)
            
            # 2. 노드 하나 뽑아서 연결관계 다 나올때까지 BFS
            while queue:
                curr = queue.popleft()
                
                # 현재 노드(curr)와 모든 노드의 연결 상태를 확인
                for next_node in range(len(isConnected)):
                    # 두 노드가 연결되어 있고(1), 아직 탐색하지 않은 노드(node_ex에 존재)라면
                    if isConnected[curr][next_node] == 1 and next_node in node_ex:
                        queue.append(next_node)
                        node_ex.remove(next_node) # 큐에 넣음과 동시에 node_ex에서 빼서 중복 탐색 방지
            
            # 연결된 녀석들을 다 찾아서 node_ex에서 뺐다면, 무리(Province) 하나를 찾은 것이므로 카운트 증가
            count += 1
            
        return count