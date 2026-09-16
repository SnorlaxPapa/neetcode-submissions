class Solution:
    def jump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return 0
        target = len(nums) - 1
        farthest = float("-inf")

        right = nums[0]
        left = 1
        jumps = 1
        while right < target:
            for i in range(left, right+1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1

        return jumps

