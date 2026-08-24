class Solution:
    def subsets(self, nums):
        result = [[]]  # 빈 집합부터 시작

        for num in nums:
            new_subsets = []  # num을 추가해서 새로 만들 부분집합

            for subset in result:
                new_subsets.append(subset + [num])

            # 새로 만든 부분집합을 기존 결과에 추가
            result += new_subsets

        return result