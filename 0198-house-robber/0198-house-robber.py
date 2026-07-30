class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums가 초항 뿐이라면 바로 리턴
        if len(nums) == 1:
            return nums[0]
        # 집을 털 때 전 집을 털었을 때의 이득과 전전 집을 털고 이번 집을 털었을 때의 이득 중 큰 쪽을 선택
        dp = [0] * len(nums) # 메모리제이션 초기화
        # 초기 항 초기화
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # 점화식
        for i in range(2, len(nums),1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[len(nums)-1]