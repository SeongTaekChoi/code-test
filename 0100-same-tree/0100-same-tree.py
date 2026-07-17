# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 값들을 차례대로 리스트에 추가한 후 일치 확인
        tree_list = []
        tree_list.append((p,q))
        # p_list와 q_list에 val들을 하나씩 append
        while tree_list:
            node1, node2 = tree_list.pop()
            # 노드 둘 모두가 none인 경우 continue
            if node1 == None and node2 == None:
                continue
            # node 둘이 일치하지 않으면 즉시 False 반환
            if node1 == None or node2 == None or node1.val != node2.val:
                return False
            # 모든 노드 값을 넣기 위함
            tree_list.append((node1.left, node2.left))
            tree_list.append((node1.right, node2.right))
        # tree_list가 다 비워질 때까지 False가 나오지 않으면 True 반환 
        return True
            
