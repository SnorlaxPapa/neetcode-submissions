class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        left = 0
        right = 0

        while (right < len(nums)):
            if (right - left > k):
                seen.discard(nums[left])
                left += 1

            if nums[right] in seen: return True
            seen.add(nums[right])

            right += 1

        return False