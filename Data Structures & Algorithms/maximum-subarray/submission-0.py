class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rolling_sum = 0
        max_sum = float("-inf")

        for num in nums:
            rolling_sum += num
            max_sum = max(max_sum, rolling_sum)

            if rolling_sum < 0: rolling_sum = 0 

        return max_sum