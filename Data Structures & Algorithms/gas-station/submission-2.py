class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        find array gas - cost
        e.g.
        [5, 8, 2, 8] - [6, 5, 6, 6] 
        = [-1, 3, -4, 2]
        

        if our net gas diff >= 0, that means there is a way
        as we run our net gas diff, we run a rolling tracker
        
        at each step,
        we treat initial as start, as we keep moving forward, if starting from there our total gas left becomes negative (not enough), then that means that any starting point including and behind our current index cannot be the starting point (as it leads to a negative sum), so we can discard them as options nd reset our gas left 
        """

        index = 0
        running_gas_tracker = 0
        total_gas_left = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total_gas_left += diff
            running_gas_tracker += diff
            if running_gas_tracker < 0:
                running_gas_tracker = 0
                index = i + 1
        
        if total_gas_left < 0: return -1
        return index