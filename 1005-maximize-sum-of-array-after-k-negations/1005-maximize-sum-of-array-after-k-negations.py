class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 1. 오름차순 정렬 후 음수가 있으면 가장 작은 수부터 순차적으로 없애감
        # 2. 음수가 모두 사라지면 남은 k가 짝수면 그냥 다 합하고, 홀수면 가장 작은 수만 부호 바꿔 더하기
        nums = sorted(nums)
        for i in range(len(nums)):
            if k == 0:
                break
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            else:
                break

        nums = sorted(nums)
        sum = 0
        if k % 2 == 0:
            for num in nums:
                sum += num
        else:
            nums[0] = -nums[0]
            for num in nums:
                sum += num
        
        return sum