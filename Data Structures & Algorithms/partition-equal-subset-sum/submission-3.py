class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1: return False
        target = total / 2
        required = {target}

        for i in range(0, n):
            if nums[i] > target: continue
            if nums[i] in required: return True
        
            for num in required.copy():
                leftover = num - nums[i]
                if leftover < 0: continue

                required.add(leftover)

            required.add(target - nums[i])
    
        return False
