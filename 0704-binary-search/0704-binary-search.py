class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 끝 인덱스
        left = 0
        right = len(nums) - 1

        # 탐색 범위가 남아 있는 동안 반복
        while left <= right:
            # 현재 탐색 범위의 중간 인덱스
            mid = (left + right) // 2

            # 중간값이 목표값과 같으면 인덱스 반환
            if nums[mid] == target:
                return mid

            # 목표값이 중간값보다 크면 오른쪽 절반 탐색
            elif nums[mid] < target:
                left = mid + 1

            # 목표값이 중간값보다 작으면 왼쪽 절반 탐색
            else:
                right = mid - 1

        # 목표값이 배열에 없으면 -1 반환
        return -1