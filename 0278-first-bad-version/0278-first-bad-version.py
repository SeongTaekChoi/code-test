# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 중앙부터 isBadVersion으로 탐색
        # bad면 그 이전 부분의 중앙 탐색, good이면 그 이후 부분의 중앙 탐색
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                # mid가 최초 불량일 수도 있으므로 범위에 포함
                right = mid
            else:
                # mid는 정상 버전이므로 제외
                left = mid + 1

        return left