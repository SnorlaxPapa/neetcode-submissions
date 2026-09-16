class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        at each step, we are provided the following information information
        We can have two states
        1) Add the current number
        2) Substract the current number 
        """
        n = len(nums)
        dp = {}
        def calculate(index, total):
            total_add = total + nums[index]
            total_minus = total - nums[index]

            if index == n - 1:
                ways = 0
                if total_add == target: ways += 1
                if total_minus == target: ways += 1
                return ways

            if (index + 1, total_add) in dp: 
                add_ways = dp[(index + 1, total_add)]
            else:
                add_ways = calculate(index + 1, total_add)
                dp[(index + 1, total_add)] = add_ways

            if (index + 1, total_minus) in dp:
                minus_ways = dp[(index + 1, total_minus)]
            else: 
                minus_ways = calculate(index + 1, total_minus)
                dp[(index + 1, total_minus)] = minus_ways

            return add_ways + minus_ways
        

        return calculate(0, 0)