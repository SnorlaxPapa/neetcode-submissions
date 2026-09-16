class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        max_length = float("-inf")

        for i in range(len(nums) - 1, -1, -1):
            local_max = dp[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    local_max = max(local_max, dp[i] + dp[j])

            dp[i] = local_max
            max_length = max(max_length, local_max)

        return max_length