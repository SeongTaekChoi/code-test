class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target이 나올 때까지 두 개씩 뽑아 차례대로 합해가기
        index = len(nums) # 요소의 개수
        for i in range(index):
            for j in range(i+1,index):
                if nums[i] + nums[j] == target:
                    index_i = i
                    index_j = j
                    break
            if i == index-1:
                break
        return [index_i, index_j]
