# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # 파이썬 기본 리스트를 스택으로 초기화
        stack = [root.left, root.right]
        
        while stack:
            # 스택의 끝에서 두 개의 노드를 꺼냄 (후입선출)
            node2 = stack.pop()
            node1 = stack.pop()
            
            # 둘 다 None이면 대칭 조건을 만족하므로 패스
            if not node1 and not node2:
                continue
            
            # 둘 중 하나만 존재하거나, 두 노드의 값이 다르면 비대칭
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # 다음 비교를 위해 대칭되는 노드 쌍을 스택에 삽입
            # 바깥쪽 노드 쌍
            stack.append(node1.left)
            stack.append(node2.right)
            
            # 안쪽 노드 쌍
            stack.append(node1.right)
            stack.append(node2.left)
            
        return True