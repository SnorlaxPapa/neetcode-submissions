class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Variable length sliding window.
        we extend until rolling sum >= target
        once >= target, we push left forward until sum <= target
        caterpillar like extension of sliding window
        """
        left = 0
        right = 0
        curr_sum = 0
        min_length = float("inf")

        while (right < len(nums)):
            curr_sum += nums[right]
            
            if curr_sum >= target:
                while (left <= right and curr_sum >= target):
                    min_length = min(min_length, right - left + 1)
                    curr_sum -= nums[left]
                    left += 1
        
            right += 1
        
        if min_length == float("inf"): return 0
        
        return min_length



