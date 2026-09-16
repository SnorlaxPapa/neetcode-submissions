class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        at step 1 -> 5 
        at step 2 -> 5 or 3, choose 5
        at step 3 -> 5+0 or 3, choose 5
        at step 4 -> 1000000 + 5 (step 2) or 0, choose 100002

        5 3 0 1000000
        
        so the core of the problem is when we step on step i,
        we are looking back at steps i-1 and i-2 and making the most optimal choice
        our tracking[i] will then represent the most optimal payoff up to that step, and the local optimal decision will become the 'global' one up to that point

        this accounts when we want to skip more than one house to find the highest payoff

        now we have an additional constraint where the houses are in a circle
        to address this, we can just run it twice, once with the 0th index and without last, and once with last and without 0
        """
        if len(nums) <= 2: return max(nums)

        def rob(nums):
            if len(nums) <= 2: return max(nums)
            prev_prev = nums[0]
            prev = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                curr = max(prev_prev + nums[i], prev) 
                prev_prev = prev
                prev = curr

            return curr

        max_one = rob(nums[:-1])
        max_two = rob(nums[1:])

        return max(max_one, max_two)

        