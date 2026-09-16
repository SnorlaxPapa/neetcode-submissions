class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        suppose we are at step n
        are steps taken is taken as
        min(step(n-1), step(n-2))
        so if we have the starting cost at steps 1 and 2,
        we can update step(2) = cost[2] + min(step[0], step[1])
        step(3) = cost[3] + min(step(2), step(1))
        step(4) = cost[4] + min(step(3), step(4)) and so on
        this is O(n) time and O(n) space 
        """
        if not cost: return 0
        if len(cost) == 1: return cost[0]
        if len(cost) == 2: return min(cost[0], cost[1])

        prev_prev = cost[0]
        prev = cost[1]

        for i in range(2, len(cost)):
            step = cost[i] + min(prev_prev, prev)
            prev_prev = prev
            prev = step


        return min(step, prev_prev)


