# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 빈 리스트가 들어오면 그대로 None 반환
        if not head: 
            return None

        # 값을 리스트로 옮기기
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
            
        # 새로운 헤드 노드 생성 (배열의 맨 마지막 값)
        new_head = ListNode(temp_list[-1])
        curr = new_head # 현재 위치를 추적할 포인터 (curr) 생성
        
        # 4. 나머지 값들을 새 노드로 만들어 줄줄이 연결
        for i in range(len(temp_list)-2, -1, -1):
            curr.next = ListNode(temp_list[i]) # 다음 칸에 새 노드 생성해서 연결
            curr = curr.next                   # 현재 위치를 다음 칸으로 이동
            
        return new_head
        