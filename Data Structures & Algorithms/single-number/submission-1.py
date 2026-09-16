import math
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        appears = 0
        for num in nums:
            appears ^= num

        return appears

