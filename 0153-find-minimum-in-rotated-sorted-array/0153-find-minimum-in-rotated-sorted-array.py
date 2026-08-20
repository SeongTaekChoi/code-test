class Solution:
    def findMin(self, nums):
        # 탐색할 범위의 왼쪽, 오른쪽 인덱스
        left = 0
        right = len(nums) - 1

        # 탐색 범위가 하나의 원소로 줄어들 때까지 반복
        while left < right:

            # 현재 탐색 범위의 중앙 인덱스
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            else:
                right = mid

        # left == right가 되면
        # 해당 위치가 배열의 최소값이다.
        return nums[left]