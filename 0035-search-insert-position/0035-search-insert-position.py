class Solution:
    def searchInsert(self, nums, target):
        # 탐색할 범위의 시작,끝 인덱스
        left = 0
        right = len(nums) - 1

        # 탐색할 범위가 남아있는 동안 반복
        while left <= right:

            # 현재 탐색 범위의 중앙 인덱스
            mid = (left + right) // 2

            # target을 찾은 경우
            if nums[mid] == target:
                return mid

            # 중앙값보다 target이 큰 경우 target은 오른쪽에 있을 가능성이 있으므로 탐색 범위를 오른쪽 절반으로 줄임
            elif nums[mid] < target:
                left = mid + 1

            # 중앙값보다 target이 작은 경우 target은 왼쪽에 있을 가능성이 있으므로 탐색 범위를 왼쪽 절반으로 줄임
            else:
                right = mid - 1

        return left