# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # node가 없는 경우
        if root == None:
            return None
        # 노드에서 left와 right 교환
        temp = root.left
        root.left = root.right
        root.right = temp

        # 재귀함수를 통해 모든 노드에 대하여 교환 수행
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        